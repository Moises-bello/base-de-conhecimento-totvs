---
article_id: 38160339968663
category: Financeiro - Novo Gestor Financeiro
content_hash: 932e814c8af0f3dd7fad2e7a50bc23270c4acc46f617b4920792b77eda6a48cf
fetched_at: '2026-06-28T22:37:41.437554+00:00'
product: protheus
section_id: 33830415324183
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - FINA713 - Erro 412: Carta de
  cobrança não parametrizada no MV_NGFCART'
type: support-article
updated_at: '2026-02-04T18:51:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38160339968663-Cross-Segmentos-Backoffice-Linha-Protheus-FINA713-Erro-412-Carta-de-cobran%C3%A7a-n%C3%A3o-parametrizada-no-MV-NGFCART
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38160339932311) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Ao processar o schedule FINA713, o sistema retorna no monitor de pendências, o erro: "412 - Carta de cobrança não está parametrizada no parâmetro MV\_NGFCART". Como resolver?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38160324086551)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da release 12.1.33.  
  
**Solução:**

O envio dos boletos por e-mail utiliza a carta de cobrança (FINA810) configurada no parâmetro **MV\_NGFCART**. Este erro ocorre quando o parâmetro não está preenchido ou quando há divergência no compartilhamento entre o parâmetro cadastrado e a tabela **FWP.**

Para que a rotina funcione corretamente, o parâmetro deve possuir no campo Filial, o mesmo nível de compartilhamento da tabela **FWP**. No processo de parametrização via Novo Gestor Financeiro, o sistema criará o parâmetro automaticamente para cada filial, caso o compartilhamento da **FWP** seja exclusivo.

**Exemplo:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38160324087575)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38160324089751)

**Informações Técnicas:**

* **Parâmetro MV\_NGFCART:** armazena o código da carta de cobrança utilizado no envio dos boletos por e-mail.
* **Tabela FWP (Cartas de Cobrança):** Tabela que armazena as cartas, onde o campo **FWP\_TXTASS** define o assunto do e-mail, que será utilizado na transmissão de boletos via Gestor Financeiro.

Para parametrizar a carta de cobrança, acesse o Novo Gestor Financeiro através do menu **Gestão Financeira → Novo Gestor Financeiro**.

Dentro do novo gestor, utilize o menu **Comunicação Online** → **Configuração de Contas.**

1. Clique no botão **Carta de Cobrança.**
2. Selecione Empresa, Unidade de Negócio ou Filial.
3. Selecione a carta de cobrança.
4. Finalize clicando no botão **Confirmar**.

![](https://tdn.totvs.com.br/download/attachments/615384255/chrome_Na1n17LDrL.gif?version=1&modificationDate=1715893099363&api=v2)

**Saiba Mais**

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA810 - Como criar um layout para a carta de cobrança?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/30978972136855-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA810-Como-criar-um-layout-para-a-carta-de-cobran%C3%A7a)

[How To | SIGAFIN - FINA713 - Envio de boleto por e-mail](https://www.youtube.com/watch?v=7UxMVQ_O6A0)

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA713 - Preparar um título contas a receber para envio de Boleto Online - API Banco do Brasil (FINA713)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7927092298903-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA713-Preparar-um-t%C3%ADtulo-contas-a-receber-para-envio-de-Boleto-Online-API-Banco-do-Brasil-FINA713)
