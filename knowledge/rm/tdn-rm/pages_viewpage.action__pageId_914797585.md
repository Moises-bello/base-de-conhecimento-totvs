---
content_hash: ef4153b85fc8e3b0321cb6590aca170aac431753d782e19f0bd859a9ab20ed48
fetched_at: '2026-06-29T00:12:06.285682+00:00'
page_id: '914797585'
product: rm
source: tdn-rm
title: Importação e Processamento de XML da Operadora
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=914797585
version: 27
---

## **CONTEÚDO**

CONTEÚDO

## **01. Visão Geral**

As rotinas descritas neste documento são responsáveis por **importar os XMLs da operadora** após o envio do lote de guias. Esse processo abrange o recebimento da confirmação com o número do protocolo, bem como as respostas dos valores **glosados** ou **acatados**.

## **02. Demonstrativo de Análise de Conta**

Após o encerramento das parciais, o prestador envia a cobrança para a operadora utilizando a mensagem **Envio de Lote de Guias** (rotina *Faturamento para Convênios*). Essa mensagem contém as guias médicas no padrão **TISS**, com os detalhes dos serviços prestados, valores cobrados e demais informações necessárias para o processamento do pagamento pela operadora.

Após o envio do lote, o prestador deve informar no sistema o **número do protocolo fornecido pela operadora**, registrando assim a confirmação do envio da cobrança. Essa informação é utilizada para o acompanhamento do processo e para consultas futuras.

Após a análise da cobrança, a operadora disponibiliza ao prestador a mensagem de **Demonstrativo de Análise de Conta**, que apresenta os valores pagos, os valores glosados (não pagos) e os respectivos motivos das glosas. Essa mensagem é essencial para que o prestador identifique quais itens foram contestados pela operadora e que podem ser objeto de recurso.

Essa rotina é responsável por **importar a mensagem de Demonstrativo de Análise de Conta no formato XML** e atualizar no sistema as seguintes informações:

* + Valores liberados pela operadora;
  + Valores glosados;
  + Motivos das glosas informados;
  + Número da guia da operadora, quando fornecido no retorno.

Durante o processo de importação, o sistema também verifica o **Número da Guia da Operadora informado no XML**. Caso esse número seja diferente do número atualmente registrado o sistema realiza automaticamente a atualização do número da guia correspondente.

Quando ocorre essa atualização, o **número anteriormente registrado é armazenado em banco**, garantindo o histórico da alteração e a rastreabilidade das informações recebidas da operadora.

Essa verificação e possível atualização são realizadas **antes do processamento das informações de valores liberados e glosas**, garantindo que a identificação da guia ocorra corretamente mesmo quando a operadora altera o número da guia no retorno do demonstrativo.

Em cenários onde existam **múltiplas guias relacionadas ao mesmo atendimento**, como nos casos de internação, o sistema considera a guia adequada para realizar a atualização das informações e dar continuidade ao processamento do demonstrativo.

Para realizar a importação do arquivo, o usuário deverá **informar todos os campos solicitados na tela e selecionar o arquivo XML no formato esperado pelo sistema**.

## **03. Recurso de Glosa e Recebimento do Protocolo**

Após a análise da cobrança pela operadora e o retorno do **Demonstrativo de Análise de Conta**, o prestador poderá iniciar o processo de **Recurso de Glosa** para contestar os itens glosados.

O processo de recurso inicia-se com o registro, no sistema, das seguintes informações:

* + - Valores que serão recursados;
    - Motivo do recurso;
    - Justificativa do recurso.

Após o preenchimento dessas informações, o prestador deverá realizar a **geração do arquivo XML de Recurso de Glosa**, que será enviado à operadora para reanálise.

Após o envio do recurso, a operadora retorna um **número de protocolo de recebimento**, que deve ser informado manualmente no sistema em tela específica de processo, para vinculação à remessa do recurso.

Nesta etapa **não existe importação de arquivo**, sendo apenas realizado o registro manual do protocolo informado pela operadora.

Atenção!

Os itens marcados como **glosa irrecuperável** **não podem ser recursados**.

---

### ***Preenchimento da Tag `<numeroGuiaOperadora>` no XML de Recurso***

De acordo com o padrão **TISS (Troca de Informação em Saúde Suplementar)**, o campo **Número da Guia da Operadora** possui preenchimento **condicionado**, podendo ou não estar presente no XML dependendo das regras de identificação da guia pela operadora.

Para suportar diferentes comportamentos das operadoras, o sistema disponibiliza o seguinte parâmetro nas **Condições Contratuais do Convênio → Eletrônico III → Geral III**:

**Copiar número da guia da operadora com base na guia do prestador no XML de recurso**

Este parâmetro define o comportamento do sistema quando **a operadora não retorna um número próprio para identificação da guia**.

---

## **Durante a geração do XML de Recurso de Glosa, o sistema seguirá as regras abaixo para preenchimento da tag `<numeroGuiaOperadora>`.**

### 1. Quando a operadora informou o número da guia

Quando o **Número da Guia da Operadora** tiver sido informado pela operadora no retorno do **Demonstrativo de Análise de Conta**, por meio da rotina de importação do XML, este número será:

* + armazenado no sistema;
  + utilizado automaticamente na geração do XML de recurso.

Neste caso, o valor retornado pela operadora **sempre terá prioridade**, independentemente da configuração do parâmetro.

### 2. Quando a operadora não informou o número da guia

Quando a operadora **não fornecer um número próprio de identificação da guia**, o comportamento dependerá da configuração do parâmetro.

* 1
  complete


  ### **Parâmetro marcado**

Se o parâmetro Copiar número da guia da operadora com base na guia do prestador no XML de recurso estiver habilitado, o sistema utilizará: <numeroGuiaOperadora> = <numeroGuiaPrestador>   
Neste cenário, o número da guia do prestador será utilizado como identificador da guia no XML de recurso.

* 2
  incomplete


  ### **Parâmetro desmarcado**

Se o parâmetro estiver **desabilitado**, e a operadora **não tiver fornecido um número de guia**, a tag: <numeroGuiaOperadora> **não será gerada no XML**, respeitando a regra de preenchimento condicionado definida pelo padrão TISS.

---

### Tabela de Decisão – Geração da Tag `<numeroGuiaOperadora>`

| Situação | Parâmetro | Número informado pela operadora | Valor gerado no XML |
| --- | --- | --- | --- |
| Operadora informou número da guia | Marcado ou Desmarcado | Sim | Utiliza o número informado pela operadora |
| Operadora NÃO informou número | Marcado | Não | Utiliza `<numeroGuiaPrestador>` |
| Operadora NÃO informou número | Desmarcado | Não | Tag não é gerada |

Atenção!

Quando a operadora **informar um número próprio de identificação da guia no Demonstrativo de Análise de Conta**, este valor **sempre será utilizado no XML de Recurso de Glosa**, independentemente da configuração do parâmetro.

Essa regra garante que o recurso seja vinculado corretamente à guia identificada pela operadora

## **04. Preenchimento do `<sequencialItem>` no XML de Recurso**

> **Disponível a partir da versão TISS 3.04.00**

O campo `<sequencialItem>` identifica cada procedimento ou despesa dentro do lote de guias. Durante o faturamento, esse número é gerado sequencialmente pelo sistema para cada item enviado.

No momento do recurso de glosa, a operadora pode exigir que os itens recursados referenciem os mesmos números sequenciais utilizados no faturamento original, garantindo a correspondência entre a cobrança e o recurso.

Para suportar esse comportamento, o sistema disponibiliza o seguinte parâmetro nas **Condições Contratuais do Convênio → Eletrônico III → Regras III**:

Este parâmetro define se o sistema deve reutilizar os números sequenciais dos itens do faturamento original ao gerar o XML de Recurso de Glosa.

* 3
  complete


  ### **Parâmetro marcado**

O sistema recupera os sequenciais dos itens gerados durante o faturamento original e os utiliza na geração do XML de recurso, garantindo que cada item recursado mantenha o mesmo `<sequencialItem>` que foi enviado na cobrança. Essa configuração é indicada para operadoras que exigem a correspondência dos sequenciais entre o faturamento e o recurso.

* 4
  incomplete


  ### **Parâmetro desmarcado**

O sistema gera sequenciais novos, a partir de 1, para cada item do recurso. Esse é o comportamento padrão, compatível com operadoras que não exigem correspondência de sequenciais.

Atenção!

Ambos os parâmetros desta seção (**Copiar número da guia da operadora** e **Utilizar sequencial do faturamento**) estão disponíveis apenas para contratos configurados com versão TISS 3.04.00 ou superior. Para versões anteriores, os campos ficam desabilitados na tela de configuração.

**05. Resposta do Recurso da Glosa**

A resposta do recurso da glosa é o retorno da operadora para o prestador, contendo a análise sobre os itens recursados anteriormente.

A importação do **XML de resposta do recurso de glosa** é uma etapa essencial no processo de gestão de contestação de glosas. Permite que os prestadores acompanhem a análise realizada pelas operadoras de saúde e tomem as devidas providências para ajustes financeiros ou novas contestações.

Ao realizar a importação do XML, o sistema identificará as contas da **Gestão de Glosa** e realizará automaticamente o controle da glosa.

Para acessar, utilize o menu:  
**Faturamento → Faturamento para Convênios → Anexo Fatura de Recurso → Importação do XML de Resposta do Recurso de Glosa**

## **06. Configurações**

Algumas configurações de contrato são utilizadas na rotina, são elas:

* + **Número de lote baseado na remessa ou fatura**  
    Esta configuração define como o número do lote será tratado. Se o número da remessa for numérico, será replicado para o número do lote. Caso contrário, o sistema valida o número da fatura; se este for numérico, será usado como número do lote. Se nenhuma das informações for numérica, o valor da remessa será considerado número do lote.
  + **Número de remessa composto**  
    Se ativada, o número da remessa será composto da seguinte forma:  
    `IDUNIDADEFATURAMENTO[XXXX] = 1 + CODIGOCONVENIO[XXXX] = 2 + NUMEROREMESSAREAPRESENTACAO 123`  
    O resultado final será, por exemplo: `"00010002123"`

O número do lote que será validado dependerá dessas duas configurações, sendo priorizada a configuração **Número de remessa composto**. Caso esta esteja marcada, será considerada; caso contrário, será considerada a configuração do parâmetro **Número de lote baseado na remessa ou fatura**. Caso nenhuma das configurações esteja marcada, o sistema considera apenas o valor informado na Remessa de Reapresentação.

Este valor será utilizado para validar se o número de lote do arquivo confere com o número da remessa, garantindo que o XML importado corresponde à remessa correta.

Atenção!

As configurações devem ser alteradas somente após todas as remessas antigas terem sido processadas. Caso contrário, as remessas enviadas com a configuração anterior podem ser processadas de forma incorreta, ocasionando erros no processamento.

## **07. Validações**

O sistema realiza as seguintes validações para garantir a integridade dos dados importados:

* + Verifica se o registro ANS é o mesmo do convênio da fatura.
  + Verifica o credenciamento do prestador principal com base no **CodigoPrestador** do arquivo.
  + Valida se o protocolo informado na fatura é o mesmo contido no arquivo (esta validação ocorre somente se o protocolo estiver informado em ambos).
  + Valida se o número do lote é igual ao número da remessa de reapresentação.
  + Valida o status da **Gestão de Glosa**; caso esteja finalizada, é necessário retornar as contas para revisão.

## **08. Processamento dos Arquivos XML**

O sistema identificará as contas e os itens recursados e fará o processamento conforme o XML importado (seja **Demonstrativo Análise Conta** ou **Resposta do Recurso**).

O processamento é realizado da seguinte forma:

* + O sistema varrerá a remessa buscando todas as contas contidas nela.
  + As contas serão identificadas inicialmente pela guia operadora, e caso não encontrada, pela guia do prestador.
  + Se a conta não estiver no arquivo, o sistema registrará no log que a conta não foi encontrada.
  + Todos os itens da conta serão carregados para comparação com os itens do arquivo. Se a conta não possuir itens, será exibido no log que a conta não possui itens.
  + Para os itens encontrados no arquivo:

    - Se o valor cobrado/recursado for menor que o valor liberado/acatado, o sistema atualizará o item na gestão de glosa com status **Glosa**.
    - Se o valor cobrado/recursado for maior ao valor liberado/acatado, o status será atualizado para **A Maior**.
    - Se o valor cobrado/recursado for igual ao valor liberado/acatado, o status será atualizado para **Liberado**.
