---
article_id: 360050966774
category: RH - Folha de Pagamento
content_hash: 6bbff60cbb6033e94eb02a30a4a2cd7d0102e6d6133e7385be582ac6b86ee825
fetched_at: '2026-06-28T22:44:16.142281+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Parâmetro MV_REFTRAB
type: support-article
updated_at: '2025-10-22T18:04:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050966774-RH-Linha-Protheus-GPE-Par%C3%A2metro-MV-REFTRAB
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24412784276375) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Configuração do parâmetro MV\_REFTRAB  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17

**Solução**Foi criado o parâmetro**MV\_REFTRAB** para estabelecer quais processos serão executados de acordo com a Reforma trabalhista.

Além de checar a data inicial de vigência (11/11/2017), a rotina deve constar no parâmetro MV\_REFTRAB para que seja executada com as alterações da Reforma.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10325051957527)

O conteúdo do parâmetro MV\_REFTRAB será o seguinte :**FSRI**, onde **F**= Férias, **S**= Contribuição Sindical, **R**= Regime Parcial e **I** = Insalubridade Gestante.   
Se, por exemplo, o conteúdo do parâmetro MV\_REFTRAB esteja "FSI", os cálculos referentes ao regime parcial serão executados sem as novas orientações da Reforma Trabalhista.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10325056161559)

Caso o parâmetro não exista no dicionário de dados, o padrão é a rotina executar a Reforma Trabalhista.

Consulte a documentação técnica dos itens da reforma que foram implementados no Protheus: [Implementação da Reforma Trabalhista](https://tdn.totvs.com/pages/viewpage.action?pageId=312149147)

**Saiba Mais**[RH - Linha Protheus - GPE - Calculo de Férias Coletivas para Funcionário maior de 50 anos não considera Dias Coletivas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/28660932698903-RH-Linha-Protheus-GPE-Calculo-de-F%C3%A9rias-Coletivas-para-Funcion%C3%A1rio-maior-de-50-anos-n%C3%A3o-considera-Dias-Coletivas)  
[RH - Linha Protheus - GPE - Mensagem ao calcular férias coletivas: O saldo de férias que restará é inferior a 5 dias. Conforme Artigo 134 parágrafo 1º da CLT, as férias não devem ser concedidas com menos de 5 dias.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/28342402593943-RH-Linha-Protheus-GPE-Mensagem-ao-calcular-f%C3%A9rias-coletivas-O-saldo-de-f%C3%A9rias-que-restar%C3%A1-%C3%A9-inferior-a-5-dias-Conforme-Artigo-134-par%C3%A1grafo-1%C2%BA-da-CLT-as-f%C3%A9rias-n%C3%A3o-devem-ser-concedidas-com-menos-de-5-dias)
