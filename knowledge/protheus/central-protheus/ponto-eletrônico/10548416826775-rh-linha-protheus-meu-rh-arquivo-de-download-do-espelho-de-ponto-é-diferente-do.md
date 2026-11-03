---
article_id: 10548416826775
category: PONTO ELETRÔNICO
content_hash: 74f328c95083d9670536c5d92b7b08046eefa72eef1f3e8f955e00730a403c4d
fetched_at: '2026-06-28T22:44:36.813326+00:00'
product: protheus
section_id: 10299685322391
source: central-protheus
title: RH - Linha Protheus - MEU RH - Arquivo de download do Espelho de Ponto é diferente
  do extraído pelo Protheus
type: support-article
updated_at: '2026-06-17T18:33:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10548416826775-RH-Linha-Protheus-MEU-RH-Arquivo-de-download-do-Espelho-de-Ponto-%C3%A9-diferente-do-extra%C3%ADdo-pelo-Protheus
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30646174914839) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Por que ao extrair o **Espelho de Ponto no Meu RH** (opção de *download* na funcionalidade de Espelho de Ponto) é **gerado** de forma **diferente** do **extraído pelo Protheus**?  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução**  
O **Meu RH**, em seu padrão, utiliza o **mesmo fonte** para *download* do **Espelho de Ponto**, que o Protheus gera através do **Módulo SIGAPON**, tendo referência ao fonte **PONR010**.   
Este fonte necessita de **Parâmetros de Impressão** para que o relatório seja gerado. Ao **Meu RH**, **não compete a possibilidade de apresentar ou alterar** estes **parâmetros de impressão**, portanto utiliza o preenchimento destes Parâmetros de Impressão de forma **fixada**, seguindo o documentado abaixo:  
[**Relatorios Meu RH Protheus**](https://tdn.totvs.com/display/NPR/Relatorios+Meu+RH+Protheus)  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10547211754647)  
  
Os **itens destacados** são os **parâmetros fixos de impressão**, que o relatório padrão gerado **pelo Meu RH** irá preencher, ou seja, o relatório/**Espelho de Ponto** final **gerado**, será baseado nessas informações. **Para chegar** ao **mesmo resultado** obtido pelo Relatório **extraído no Meu RH**, faz-se **necessário** extraí-lo pelo Protheus, **certificando-se** de **preencher todos os parâmetros** conforme a **documentação** acima.  
  
**Contudo**, o **Meu RH** **pode utilizar o** ***RDMake*** **IMPESP**, caso ele seja compilado no **Repositório (RPO) do REST**, será executado no lugar do fonte padrão PONR010. Com isso, o relatório de **Espelho de Ponto permite ser customizado** de acordo com as necessidades da empresa.  
  
Para utilizar o ***RDMake*** **IMPESP** no Meu RH, basta:  
**1.** **Baixar** o pacote de **Expedição Contínua do RH** mais recente:   
[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854)  
**2.** **Encontrar** o fonte **IMPESP.PRX** dentro do diretório "***rdmakes***";  
**3.** **Adicionar** o fonte em seu projeto do **VS Code** e **compilar**, após ajustes necessários no fonte.  
  
**Saiba Mais**  
[**RH - Linha Protheus - MEU RH - Aprenda sobre o MEU RH e como fazer a implantação**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036164214)  
[**CLIQUE AQUI para acessar mais artigos e FAQs sobre o MEU RH**](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI para acessar a documentação de referência sobre o MEU RH**](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
