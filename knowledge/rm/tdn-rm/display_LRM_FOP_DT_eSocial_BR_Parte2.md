---
content_hash: 6c169c2b901c32f2965ee523ba5b5bb3b1353427de9a259a085ee4af0dd50e81
fetched_at: '2026-06-29T00:06:25.568386+00:00'
page_id: '224441256'
product: rm
source: tdn-rm
title: FOP_DT_eSocial_BR_Parte2
type: documentation
url: https://tdn.totvs.com/display/LRM/FOP_DT_eSocial_BR_Parte2
version: 6
---

# ESOCIAL PARTE 2

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **TOTVS Folha de Pagamento** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *eSocial* |  | |
| **Versão/Release:** | Bibliotecas RM 11.52.61 **|** 11.53.74 **|** 11.82.33 **|** 11.83.54 |

## Descrição

Este documento serve para que os usuários possam configurar dados que completam o eSocial

## Procedimento para Utilização

## Cadastro de Funcionários

### Estado Civil

No campo Estado Civil tem como opção de preenchimento os itens E – União Estável e S – Separado.

### Tipo de Funcionário

O campo Tipo de Funcionários foi reposicionado para as informações de Registro, antes fazia parte das informações de Salário/Jornada.

Sendo que nas informações de Salário / Jornada o Tipo de Funcionário também será demonstrado, porém, conforme o preenchimento deste mesmo campo nas informações de Registro.

### Trabalhador Temporário

No cadastro de Funcionários, na guia Informações Contratuais - Registro, quando o campo Tipo de Funcionário for preenchido com B – Temporário com redução de encargos, F – Temporário / Comissionista ou P – Temporário está habilitada a aba Trabalhador Temporário para devido preenchimento das informações.

O campo Motivo de Contratação Trabalhador Temporário tem as opções:

• Acréscimo extraordinário de serviços;  
• Necessidade transitória de substituição de seu pessoal regular.

### Funcionário Substituído

Sendo um funcionário do tipo B – Temporário com redução de encargos, F – Temporário / Comissionista ou P – Temporário, quando na aba Trabalhador Temporário o campo Motivo de Contratação Trabalhador Temporário for preenchido com a informação Necessidade transitória de substituição de seu pessoal regular, o campo Chapa do Funcionário Substituído será habilitado. Informar neste campo a chapa do funcionário que foi substituído temporariamente.

### Sucesso de Vínculo

Conceitualmente, a sucessão de vínculos será proveniente quando o tipo de admissão do funcionário for por transferência entre empresas do mesmo grupo econômico, ou, sua admissão for proveniente por uma sucessão, incorporação, cisão ou fusão.   
Há duas maneiras de informar a Sucessão de Vínculo: diretamente pelo cadastro do funcionário, ou, por meio do processo de transferência de funcionários que é realizado ao cadastrar uma Rescisão por transferência.

• Através do cadastro de Funcionários, na guia Registro, quando o campo Tipo de Admissão estiver preenchido com T – Ent Transf sem ônus p/ Cedente a aba Sucessão de Vínculo será habilitada.   
Se o campo Admissão por sucessão, incorporação, cisão ou fusão for marcado, indicará que a transferência é proveniente de uma sucessão, incorporação, cisão ou fusão de empresas.   
Se este campo não for marcado, indicará que a transferência é proveniente entre empresas/filial do mesmo grupo econômico.

Na aba Sucessão de Vínculo, o usuário deverá preencher os dados: CNPJ Empregador Anterior, Matricula Anterior e Data Início do Vínculo.

Nos módulos de Rescisão ou Rescisão Coletiva, os dados de Sucessão de Vínculo gerados automaticamente. Basta preencher o campo Tipo de Demissão com a informação 5 – Transferência sem ônus para Cedente.   
Se o campo Sucessão de Vínculo for marcado, indicará que a transferência é proveniente de uma sucessão, incorporação, cisão ou fusão de empresas.   
Se este campo não for marcado, indicará que a transferência é proveniente entre empresas/filial do mesmo grupo econômico.

O processo de transferência, quando finalizado, irá preencher no cadastro destino do funcionário os dados da Sucessão de Vínculo, automaticamente.

### Tipo de Regime de Jornada

O controle do tipo de Regime de Jornada será realizado pelo TOTVS Automação de Ponto. Quando o funcionário Usar Cartão de Ponto, para o eSocial, tipo de Regime de Jornada será considerado como Submetidos a Horário de Trabalho (Cap. II da CLT).   
Quando o funcionário não utilizar cartão de ponto, o controle deve ser feito pelo usuário do TOTVS Automação de Ponto por meio do processo Deixar de utilizar o cartão de Ponto, localizado na tela de visão do cadastro de Funcionários.

Ao abrir a tela do processo Deixar de utilizar o cartão de Ponto, informar no campo Data de Início a data de quando o funcionário deixou de utilizar o cartão de ponto e informar um dos dois tipos de Regime de Jornada:

• Atividade Externa especificada no Inciso I do Art. 62 da CLT;

• Funções especificadas no Inciso II do Art. 62 da CLT.

### Salário Variável

No cadastro de Funcionários, guia Salário/Jornada, foi implementado o campo para registrar informações sobre o Salário Variável, que será habilitado quando, o tipo de funcionário for F – Temporário/Comissionista, M – Misto ou O – Comissionista

### Deficiência Intelectual

Na guia RAIS, foi incluído no tipo de deficiência Deficiente Intelectual.

### Histórico de Afastamento - Indicador de Efeito Retroativo

No histórico de afastamento do funcionário, caso haja alteração do campo Motivo de Afastamento, ao clicar no botão Salvar ou OK, o sistema irá apresentar a mensagem de confirmação A alteração do motivo tem efeito retroativo à data de afastamento original, com as opções de resposta Sim / Não.

No anexo será criado o Histórico de Motivo de Afastamento.

Se na mensagem clicar em Sim, no histórico da alteração, o campo Indica Efeito Retroativo ficará marcado, do contrário, não.

As informações podem ser editadas pelo usuário.

### Anexo Vínculos Empregatícios com outras Empresas

No cadastro de Funcionários foi implementado o anexo Folha de Pagamento / Vínculos Empregatícios com outras Empresas

Neste, os campos Tipo de Inscrição, Número de Inscrição, Mês Competência, Ano Competência, Valor da Remuneração e Valor do Desconto INSS devem ser informados.   
As informações cadastradas terão fins informativos ao eSocial e não incidirão para o Cálculo no TOTVS Folha de Pagamento.

### RM Portal - Endereço do Funcionário

No Portal RM, em Meus Dados / Dados Cadastrais / Endereço, foi incluído o campo Tipo de Rua.

Para informar o Tipo de Rua, clicar em Alterar Endereço e selecionar a informação pertinente.

Observação: De acordo com os parâmetros do RM Portal, a alteração pode ser persistida diretamente na base de dados, ou ficar pendente de aprovação, neste caso, o usuário do sistema deve executar o processo Aprovações de Alt. Cadastrais disponível na guia Administração de Pessoal do TOTVS Folha de Pagamento.

### Portal RM - Documentos - Dados CNH

No Portal RM foram incluídos os campos Data de Expedição e Órgão Emissor nos dados da CNH, para que o próprio funcionário preencha as informações, para isto, basta clicar em Alterar Dados da Carteira de Motorista.

Os campos Data emissão e Órgão Emissor estão habilitados para edição.

Observação: De acordo com os parâmetros do RM Portal, essa alteração pode ser persistida diretamente na base de dados, ou ficar pendente de aprovação, neste caso, o usuário do sistema deve executar o processo Aprovações de Alt. Cadastrais disponível na guia Administração de Pessoal do TOTVS Folha de Pagamento.

### Cadastro de Seções

No cadastro de seções, na aba Dados p/ INSS, foi implementado o campo eSocial Indicativo de Substituição da Contribuição Patronal da Obra de Construção Civil, o qual deve ser preenchido com as opções Contribuição Patronal Substituída, ou, Contribuição Patronal Não Substituída.

Este campo acima será habilitado especificamente quando todas as condições abaixo forem verdadeiras:

 Classificação Tributária no cadastro de Informações do Empregador estiver preenchida com 12 – Empresa enquadrada nos art. 7º a 9º da lei 12.546/2011, exceto aquelas enquadradas na classificação tributária 05;  
 Campo Indicativo Obra do cadastro de Empregador estiver preenchido com 1 –Empresa Construtora;

 No cadastro da seção, campo Tipo Lotação preenchido com 02 – Obra Própria Pessoa Jurídica, 03 – Obra de Construção Civil (Empreitada Parcial ou Subempreitada) ou 22 – Obra Própria Pessoa Física

### Acesso ao cadastro de Endereço

A partir dessa versão, foi incluído na guia eSocial do TOTVS Folha de Pagamento a opção Endereços e correlacionados, conforme consta na imagem abaixo.

### Classificação de Nações

A associação de Países às Nações, a partir dessas versões, deverão ser realizadas pelo cadastro Classificação de Nações do TOTVS Folha de Pagamento, disponível na guia eSocial / Endereços.   
Observação: A funcionalidade de associação de Países às Nações, em versões anteriores, era realizada por meio do Parametrizador.   
Editando a Nação 10 – Brasileira, por exemplo, no campo Nome do País associar BRA – Brasil.

Conforme abaixo

### Validação da Base de Dados

O menu Validação da base de dados, está disponível nas versões 11.82 e superiores.   
Nesta funcionalidade foi implementado o parâmetro Executar verificação campos do eSocial para consistir os dados de funcionários que serão gerados no eSocial.   
Ao marcar o parâmetro, será habilitada a opção para verificar dados pertinentes para a geração do evento S – 2100 – Cadastramento Inicial do Vínculo.   
As informações após o processamento da Validação da base, estará consolidado no log eSocial.

### Cadastro de Cliente/Fornecedor

No cadastro Cliente/Fornecedor foi implementada na Administração de Pessoal

Os campos implementados são:  
• Tipo de Lotação, se preenchido com os tipos 02 – Obra Própria – Pessoa Jurídica, ou, 22 – Obra Própria – Pessoa Física, será habilitado o campo CNO da obra própria, o qual deve ser preenchido.

Quando o Tipo de Lotação for preenchido com o tipo 03 – Obra de Construção Civil (Empreitada Parcial ou Subempreitada), serão habilitados os campos CNO da obra própria, além dos campos, Informações do Contratante e Informações do Proprietário que devem ser preenchidos com os respectivos CNPJ ou CPF.   
Se o Tipo de Lotação for preenchido com os tipos 04 - Tomador de Serviço - Cessão de Mão de Obra, inclusive contratante de cooperativa de trabalho (PJ), ou, 05 - Tomador de Serviço - trabalho temporário - substituição de pessoal, ou, 06 - Tomador de Serviço - trabalho temporário - serviços extraordinários, não serão habilitados outros campos.

### Agente

No cadastro Agentes Agrupadores do TOTVS Segurança e Saúde Ocupacional foi implementado o campo Agente Agrupador eSocial, onde se deve classificar o tipo de Agente Nocivo, podendo ser B – Biológico, E – Ergométrico, F – Físico, M – Mecânico/Acidentes ou Q – Químico.

### Fonte Geradora

No cadastro Fonte Geradora, caso possua itens cadastrados antes das implementações do eSocial, a eles é preciso associar, no campo Cód. ESocial, o item estabelecido no manual do eSocial.

É importante salientar que todos os itens próprios do eSocial já estão cadastrados e com o campo Cód. ESocial preenchido por padrão.

### Tipos de Agente

No cadastro de Tipos de Agente foi implementado o campo Tipo de Agente Nocivo eSocial onde se deve relacionar os itens da Tabela 7 - Riscos Ocupacionais Específicos do manual eSocial.

### CAT - Tipo sem Lesão

Para cadastrar o CAT com um Incidente, caso não haja lesão à vítima, foi criado no cadastro de Tipos de Ocorrência, o item Sem Lesão para classificar o Tipo de Acidente.

O cadastro do Tipos de Ocorrência está localizado no TOTVS Segurança e Saúde Ocupacional , guia CAT / Tipos de Ocorrência, nele é possível incluir o tipo Sem Lesão.

Os cadastros existentes de Tipos de Ocorrência devem ser editados e definidos com um desses Tipos de Acidente:

• Típico;  
• Trajeto;  
• Doença;  
• Sem Lesão.

Observação: Os CAT’s registrados no sistema com o campo Cód. Tipo Ocorrência preenchido com Tipo de Ocorrência sem lesão, não são considerados para o eSocial.

### Reabertura do CAT

Foi implementado no cadastro do CAT os campos Data Cat de Origem e Número Cat Origem, que serão habilitados quando o campo Tipo da CAT for preenchido com 2 – Reabertura.

A reabertura do CAT ocorre quando há reinício de tratamento ou afastamento por agravamento de lesão de acidente do trabalho ou doença ocupacional comunicado anteriormente ao INSS.  
 No CAT de reabertura deverão constar as mesmas informações da época do acidente, exceto quanto ao afastamento, último dia trabalhado, atestado médico e data da emissão, que serão relativos à data da reabertura. Dessa forma, havendo necessidade de reabertura, deverá incluir novo cadastro para CAT deste tipo.
