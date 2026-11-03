---
article_id: 360012457072
category: RH - Recibos e Cheques
content_hash: 3a2542541149f892120f5654c1c1e888518ddf8e1ca1d109ef8e72d258707a7f
fetched_at: '2026-06-28T22:43:29.542881+00:00'
product: protheus
section_id: 360011909573
source: central-protheus
title: RH - Linha Protheus - GPE - Geração e Impressão de Cheques
type: support-article
updated_at: '2024-07-23T14:04:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012457072-RH-Linha-Protheus-GPE-Gera%C3%A7%C3%A3o-e-Impress%C3%A3o-de-Cheques
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25102566570263) Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida** **GPER280** - Geração e Impressão de Cheques  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Montar a estrutura da impressão: Para montar a estrutura do cheque, deverá ser realizada através do módulo **Financeiro**, rotina **CFGX015 - Miscelânea/Arquivos/Cheque,** de preferência sugerimos o acompanhamento de um consultor *in loco* ou de um profissional do setor Financeiro da empresa, para auxiliar na estruturação do *layout* correto.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6166425347095)

Exemplo:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6166786086295)

Após confirmar, selecione a opção desejada:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6166802259351)  
  
**Cadastro do funcionário**: No **cadastro do funcionário,** não existe uma funcionalidade que permita selecionar a opção pagamento via cheque ou banco, porém, no **cadastro do funcionário** deverá estar cadastrado o número da Conta/Agência e Banco que se destina o pagamento devido, pois a real forma de pagamento será informada pelo usuário no momento de emissão do cheque ou arquivo bancário.  
  
**Gerar o Cheque:**para um determinado funcionário em prol de um valor devido, seja ele, Saldo de salário, Adiantamento, 13° salário. Execute a rotina **GPER280**- **Relatórios/ Recibos- Cheques/Emissão de Cheque,** esta funcionalidade permite que seja escolhido qual tipo de pagamento será efetuado, a ordem de impressão do cheque, se será por matrícula, centro de custo etc... se a impressão do cheque será feito com base no líquido da folha ou por verba [**Importante:**](http://tdn.totvs.com/pages/viewpage.action?pageId=271412515)

* A numeração do cheque será informada manualmente pelo usuário.  
  ![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6177834245655)
* O sistema grava o último número do cheque informado nos parâmetros.
* O sistema não permite a emissão de dois cheques para a mesma ordem numérica.

**Impressão do Cheque:**  
Para realizar a impressão do Cheque, deverá ser configurada a impressora através do parâmetro MV\_IMPCHEQ.  
**MV\_IMPCHEQ:**Impressora padrão para impressão de Cheques.  
Exemplo:

**![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6178265483927)**

**Saiba mais**

[RH - Recibos e Cheques](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011909573-RH-Recibos-e-Cheques)

[MP - GPE0229 - GPER280 - Geração e Impressão de Cheques](http://tdn.totvs.com/pages/viewpage.action?pageId=233736565)
