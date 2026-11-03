---
content_hash: 1493796a255faa2c38d34f6b7884f9856906eeceb92741e4134ea4193cecb56b
fetched_at: '2026-06-29T00:05:48.679600+00:00'
page_id: '1027814500'
product: rm
source: tdn-rm
title: Gerenciador de Relatórios - Smart View
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1027814500
version: 7
---

false

**A partir das Versões:**

* [Vídeo How To](https://www.youtube.com/watch?v=vk-rHt6BnVQ)

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

O **Gerenciador de Relatórios Smart View**, é uma nova central de processamento desenvolvida para otimizar a extração e o acompanhamento de relatórios integrados ao RM.  
Esta ferramenta foi projetada para centralizar a geração de relatórios específicos para um determinado funcionário ou vários funcionários, facilitando o envio de alguns parâmetros do funcionário(s) desejado(s). Com o gerenciador, será possível executar a geração tanto síncrona ou assíncrona(segundo plano).

* **Processamento em Segundo Plano:** Permite que o usuário continue navegando no sistema enquanto o relatório é gerado, eliminando o tempo de espera em tela.
* **Gestão de Unicidade:** O sistema suporta a integração de diversos relatórios distintos, garantindo que não haja duplicidade de um mesmo modelo (ID de relatório) na central de gerenciamento.
* **Filtros Avançados e Dinâmicos:** Possibilita refinamentos precisos por chapa, filial e períodos específicos, garantindo que os dados extraídos reflitam a realidade da Folha de Pagamento em tempo real.
* **Notificação Automatizada:** Integração com os parâmetros globais de e-mail do sistema para envio automático do arquivo gerado, tanto para o usuário solicitante quanto para o e-mail cadastrado no registro do funcionário.

É fundamental notar que esta ferramenta é destinada à **otimização do fluxo de entrega de informações**. Enquanto os processos padrão de geração direta permanecem ativos, o Gerenciador Smart View oferece uma camada adicional de governança, mantendo um histórico de execuções (Jobs) com exclusão automática programada para registros com mais de 5 dias, garantindo a integridade e o desempenho do banco de dados.  
Este processo visa garantir a conformidade com as demandas de RH e DP, oferecendo uma forma moderna e escalável de gerir o output de dados, reduzindo o impacto no servidor e melhorando a experiência do usuário final.

## **02. EXEMPLO DE UTILIZAÇÃO**

11ParametrizaçãoParametrização

A disponibilidade do Gerenciador de Smart View é controlada por tags de segurança. É possível restringir ou liberar o acesso conforme a necessidade do negócio.

* **Caminho para Configuração:** Segurança | Perfil | Sistema: Folha de Pagamento | [Selecionar Perfil] | Relatórios | Gerenciador Smart View.

Atenção

Certifique-se de que apenas os perfis responsáveis pela gestão de dados tenham permissão de edição, mantendo o perfil de consulta para usuários finais.

true2Configuração e Informações complementaresConfiguração e Informações complementares

Para que os relatórios cheguem aos destinatários, o servidor SMTP deve estar configurado.

# 1 - Envio de E-mail

* **Caminho:** Ambiente | Parâmetros Globais | Envio de E-mail.

**Validação:** Teste a conexão para garantir que o RM tem permissão de disparar mensagens.

# 2 - Relatório integrado e unicidade

* O Gerenciador Smart View permite a integração de **múltiplos relatórios distintos** para atender às diversas necessidades da Folha de Pagamento.
* **Regra de Unicidade:** Cada relatório (ex: FOPTRP0001) só pode ser integrado **uma única vez**. Não é permitida a repetição do mesmo objeto de relatório na estrutura do gerenciador.
* **Regra de Matrícula:** É fundamental ressaltar que a **matrícula do funcionário depende da filial**. Filtros que ignoram a hierarquia de coligada/filial podem retornar dados inconsistentes ou erro no processamento.

Nesta etapa de implementação, o Gerenciador Smart View disponibiliza os seguintes relatórios para geração: **FOPTRP0001** (Aviso de Férias), **FOPTRP0006** (Histórico Salarial), **FOPTRP0013** (Recibo de Pagamento), **FOPTRP0019** (Declaração de Encargos de Família), **FOPTRP0020** (Lista de Dependentes) e **FOPTRP0022** (Ficha de Funcionário).

### 2.1 Modo de Geração

O Gerenciador oferece diferentes formas de processamento:

* **Geração Simples:** Exibe a lista de relatórios integrados disponíveis para execução imediata.

* **Geração em Lote:** Permite o processamento de múltiplos registros ou funcionários de uma só vez, otimizando o tempo do usuário.

* **Filtros Avançados:** Utilizados para refinar a massa de dados (ex: por período, chapa ou situação), garantindo que apenas as informações necessárias sejam processadas.

# 3 - Recebimento e Notificação

O sistema utiliza dois fluxos distintos para o envio de e-mails:

1. **Usuário Logado:** O relatório é enviado automaticamente para o e-mail vinculado ao usuário que disparou o processo no RM.
2. **E-mail do Funcionário:** Para relatórios individuais, o sistema busca o endereço no campo **E-mail** da tabela `PPESSOA`.

# 4 - Gerenciamento em Segundo Plano

Todo relatório gerado é enviado para uma fila de processamento em segundo plano.

* **Monitoramento de Status:** Explicação dos status (Em fila, Executando, Concluído ou Erro).
* **Políticas de Retenção:**
* **Exclusão Automática:** Atualmente, o sistema realiza a limpeza de registros antigos (com mais de **5 dias**).
* **Nota Importante:** Este período de retenção é temporário e poderá sofrer alterações em atualizações futuras conforme a necessidade de armazenamento de dados.

# 5 - Filtros Avançados

### 5.1 Filial

* **Filial (Obrigatório):** Este parâmetro define a unidade de negócio específica da qual os dados serão extraídos.

### 5.2 Matricula

* Permite filtrar o relatório por um número de identificação específico do colaborador dentro da filial selecionada.

5.3 Centro de Custo

* **Centro de Custo:** Utilizado para agrupar e filtrar os resultados com base nos setores ou unidades orçamentais da empresa, facilitando a análise de custos por departamento.

5.4 Parâmetro: CPF

* O parâmetro **CPF** é de preenchimento **opcional**. Caso seja adicionado apresentará somente o CPF digitado.5.4 Parâmetro: CPF

### 5.5 Situação

* Permite selecionar o status atual do colaborador (ex: Ativo, Demitido, Afastado) para filtrar quem deve constar no relatório.

### 5.6 Categoria

* Utilizado para segmentar os colaboradores por tipo de vínculo ou classificação funcional (ex: Mensalista, Horista, Estagiário).

### 5.7 Data de admissão De\Até

* Estes campos de data permitem definir um intervalo temporal específico baseado na data de contratação, filtrando colaboradores que entraram na empresa dentro do período estipulado.

Atenção

**Para aplicar o filtro avançado é necessário informar primeiramente o parâmetro filial.**

# 3 - Apresentação dos dados e exemplo de uso

Após Aplicar Filtros, será exibida as seguintes colunas: 

| Coluna | Campos |
| --- | --- |
| Situação | PFUNC.CODAITUACAO |
| Filial | PFUNC.CODFILIAL |
| Matricula | PPESSOA.CODUARIO |
| Nome | PPESSOA.NOME |
| CPF | PPESSOA.CPF |
| Dt. Admissão | PPESSIA.DATAADMISSAO |
| Categoria | PFUNC.CODCATEGORIA |
| Centro de custo | PFUNC.CODCUSTO |

A listagem permite a seleção de funcionários via **checkbox** e o gerenciamento de relatórios individuais através do ícone de **elipse horizontal** presente em cada linha.

Após selecionar o **relatório** desejado, aplique os filtros necessários e acione o comando de geração para iniciar o processamento dos dados e download do relatório.

### 5.1 Geração em lote em segundo plano

| Coluna | Campos |
| --- | --- |
| Status | PGERSMARTVIEW.STATUS |
| Já Baixou | PGERSMARTVIEW.DOWNLOAD |
| Data | PGERSMARTVIEW.RECCREATEON |
| Matricula | PGERSMARTVIEW.CHAPA |
| Nome | PPESSOA.NOME |
| Relatório | PGERSMARTVIEW.ARQUIVO |
| Descrição | PGERSMARTVIEW.DESCRICAORELATORIO |

A listagem permite a seleção múltipla de funcionários via **checkbox**, possibilitando a **geração em lote** simultânea de relatórios. Uma vez solicitada, a execução ocorre em **segundo plano**, liberando a navegação no sistema durante o processamento. Para acompanhar o progresso e realizar o download, acesse o **ícone de notificação (sino)** no canto superior direito da tela. Na central de notificações, cada requisição exibirá informações detalhadas, como descrição e status. Inicialmente, o registro será apresentado com o status **'Em Fila'**, progredindo para **'Gerado'** assim que concluído. Após a finalização, a opção de **download** ficará disponível ao final da linha correspondente à requisição.

## **03. TABELAS UTILIZADAS**

* PPESSOA
* PFUNC
* PGERSMARTVIEW
