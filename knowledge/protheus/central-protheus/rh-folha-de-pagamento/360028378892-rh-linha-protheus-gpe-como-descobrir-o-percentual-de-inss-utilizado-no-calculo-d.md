---
article_id: 360028378892
category: RH - Folha de Pagamento
content_hash: 246f608b38be44181f72b2166b8bc7661b1ce184a191003ef55caf99e82015f4
fetched_at: '2026-06-28T22:44:13.368581+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como descobrir o percentual de INSS utilizado no
  calculo da provisão
type: support-article
updated_at: '2024-09-12T11:33:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028378892-RH-Linha-Protheus-GPE-Como-descobrir-o-percentual-de-INSS-utilizado-no-calculo-da-provis%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26319646913303) Tempo aproximado para leitura: 00:03:00 min**

**Dúvida**Como descobrir percentual de **INSS** utilizado no calculo da provisão ?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**

Pegar o valor do **INSS** gerado no relatório de provisões, dividir pelo valor da coluna **Total Férias** e multiplicar por 100;

Exemplo:  INSS 882,83 / 10.730,66 Total férias X 100= 8.2273%.

Este percentual também pode ser visto através da rotina **Atualizações / Definições cálculo / Manutenção de tabelas/Tabela S037:**

S037 - %Empresa + % Acidente de Trabalho

S038 - % Terceiros

Soma-se o percentual do campo Terceiros 5,8 + o percentual do campo Acid Trabalho 3,000 = 8,800%

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029098011)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029098111)

Para empresas não optantes pelo simples nacional, deverá ser considerado também o campo %Empresa= 20%, logo, se não for optante pelo simples o sistema deverá considerar 28,2273%.

Para saber se a empresa é optante ou não do simples nacional, basta acessar o parâmetro 14 e verificar o conteúdo do campo abaixo:

No caso, desta demonstração de cálculo o cliente é optante do simples nacional, logo, o percentual que será utilizado no cálculo da provisão será os percentuais dos campos **“%Terceiros”** +**“Acid Trab.”** de acordo com os campos **“Ano”**e**“Mês (exemplo filial 06).**

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029333691)

INSS Provisão férias: Provisão de férias + 1/3 \* (% INSS empresa + terceiros + acidente de trabalho) %

750 + 250 = 1.000

1000 \* 28,8% = 288,00

**Mais informações sobre provisão no link abaixo:**

**<http://tdn.totvs.com/pages/viewpage.action?pageId=272405840>**

**Saiba Mais**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)

[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
