---
article_id: 360016503491
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: c2254d4db1e4f73ce2ab9a9f7ac9bf6749858cf5664c968033190a60564ff8ef
fetched_at: '2026-06-28T22:37:20.006201+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como gerar contratos
  no Gestão de Contratos a partir de uma Cotação?
type: support-article
updated_at: '2026-01-08T18:44:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016503491-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-gerar-contratos-no-Gest%C3%A3o-de-Contratos-a-partir-de-uma-Cota%C3%A7%C3%A3o
---

**Dúvida**  
Como gerar contratos no módulo Gestão de Contratos a partir de uma Cotação ?  
  
**Ambiente**  
Microsiga Protheus – a partir da versão 12.1.17]  
  
**Solução**

Realizar o processo conforme script abaixo e validar os resultados:

**1-** Efetuar Amarração Produto x Fornecedor (MATA061);

**2-** Cadastrar uma Solicitação de Compras (MATA110);

**3-** Gerar a Cotação/ Botão Gera Cotação (MATA131);  
(utilizar F12 para definir Contrato (GCT) ao finalizar a cotação)

![cota__o_contrato.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360103580773)

**4-** Efetuar a Atualização de Preços da Cotação (MATA150);  
(outras ações/atualizar)

**5-** Realizar a Análise da Cotação (MATA161) salvando com o Fornecedor Vencedor;  
Observar no cabeçalho da tela da Análise de Cotação a opção "Tp. Doc." como "Contrato (GCT)":

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500002539822)

**6-** Preencher os processos padrão do Contrato (p.ex. Tipo, Cond.Pgto entre outros)/ Salvar o Contrato.

**7-** Caso após criar o contrato precise alterar o mesmo e seja apresentado o ***Help: CN300TPCTR*** é possível que esteja tentando informar um tipo de contrato Flexível em um contrato que originalmente foi criado como Fixo.No sistema, foi criada a validação com o ***HELP: CN300TPCTR*** para que contratos gerados por cotação (ou edital) não sejam alterados de fixo para flexível, tendo assim uma maior segurança no processo de cotação, assim todo o processo cotado, como por exemplo valor, quantidade e informações de fornecedor, e prazos, não sejam alterados de forma indevida.

Foi disponibilizado também o parâmetro **MV\_VLDTPFI** que permite desativar a validação do tipo de contrato, possibilitando a inclusão de um contrato de qualquer tipo durante o processo de cotação conforme link - [Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Parâmetro MV\_VLDTPFI que permite Gerar Contratos diferentes de Fixo a partir de uma Cotação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11883346619671-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Par%C3%A2metro-MV-VLDTPFI-que-permite-Gerar-Contratos-diferentes-de-Fixo-a-partir-de-uma-Cota%C3%A7%C3%A3o?source=search)

***Obs1:***

Ao gerar um contrato da rotina "gera cotação", não é possível proceder com inclusão de planilhas bem como alterar campos de fornecedor, produto, etc do contrato devido para que seja mantida a integridade com os dados informados na rotina que originou o contrato.

***Obs2:***

Caso não se tenha definido a opção "Contrato (GCT)" no "passo 3", poderá realizar essa escolha através do campo "Tp. Doc." da Análise de Cotação demonstrada no "passo 5".

***Parâmetros associados:***  
***MV\_SELFOR*** - Parâmetro que indica se o Comprador poderá fazer seleção dos Fornecedores

***MV\_TPPLA*** - Tipo de Planilha para Geração de Contrato via Analise de Cotação (Obrigatório o Preenchimento para este processo)

***Obs3:***

Conforme o conceito do SIGAGCT, para os contratos gerado que veem de cotação, **não se deve informar** um **Tipo de Planilha de Serviço** no parâmetro ***MV\_TPPLA,** n*ão podendo assim ser utilizado este Tipo de planilha de Serviço do artigo abaixo para a geração de contrato a partir de cotação:

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Quais as configurações para utilização de Contrato / Planilha de Serviço no Gestão de Contratos ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053570234-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Quais-as-configura%C3%A7%C3%B5es-para-utiliza%C3%A7%C3%A3o-de-Contrato-Planilha-de-Servi%C3%A7o-no-Gest%C3%A3o-de-Contratos)

***Saiba Mais:***

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Parâmetro MV\_VLDTPFI que permite Gerar Contratos diferentes de Fixo a partir de uma Cotação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11883346619671-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Par%C3%A2metro-MV-VLDTPFI-que-permite-Gerar-Contratos-diferentes-de-Fixo-a-partir-de-uma-Cota%C3%A7%C3%A3o?source=search)

[MT161CNT - Geração de Contrato na análise de cotação](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=496804484)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001302787-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-)
