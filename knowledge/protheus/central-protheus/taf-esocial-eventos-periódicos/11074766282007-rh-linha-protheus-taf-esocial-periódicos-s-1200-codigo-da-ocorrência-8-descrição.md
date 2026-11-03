---
article_id: 11074766282007
category: TAF - eSocial - Eventos Periódicos
content_hash: 1714e5fed8f350d5ac446882f718e1b857288b952be8504cd94e66a14e41b877
fetched_at: '2026-06-28T22:45:18.938153+00:00'
product: protheus
section_id: 1500001536901
source: central-protheus
title: 'RH - Linha Protheus - TAF - eSocial  - Periódicos -  S-1200 - Codigo da Ocorrência:
  8 - Descrição : Grupo #39;Grau de Exposicao a Agentes Nocivos#39; deve ser preenchido.'
type: support-article
updated_at: '2026-06-25T11:42:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11074766282007-RH-Linha-Protheus-TAF-eSocial-Peri%C3%B3dicos-S-1200-Codigo-da-Ocorr%C3%AAncia-8-Descri%C3%A7%C3%A3o-Grupo-39-Grau-de-Exposicao-a-Agentes-Nocivos-39-deve-ser-preenchido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23703960980887) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Ao transmitir o evento S-1200, retorna a inconsistência, pelo governo.

*Tipo: Erro - Codigo da Ocorrência: 8 - Descrição : Grupo[#39](https://totvssuporte.zendesk.com/agent/tickets/39);Grau de Exposicao a Agentes Nocivos#39; deve ser preenchido.*

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial- Periódicos - S-1200 - Remuneração de trabalhador vinculado ao Regime Geral de Previdência Social (TAFA250)- Todas as versões  
  
**Solução**Para corrigir a inconsistência, pelo TAF:

1. Gere o XML do TAF, do evento S-1200 inconsistente

[RH - Linha Protheus - GPE - eSocial - Como gerar ou comparar os arquivos XML do SIGAGPE e SIGATAF dentro do módulo SIGATAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026656853)

2. Abra o XML em um navegador de internet,  ou software apropriado.

3. Localize os códigos de lotação, através da tag **<codLotacao>,** para cada um dos códigos de lotação, deve existir uma tag **<grauExp>** preenchida. Como no exemplo abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11073950728471)

**ATENÇÃO:** Se o evento S-1200 possuir pagamentos em períodos anteriores, os mesmos também devem possuir a tag **<grauExp>**preenchida para cada uma das lotações/ meses citados;

4. Localizada a lotação que não possui a tag **<grauExp>,**a correção pode ser realizada pela rotina TAFA250, referente ao evento S-1200;

5. Entre na rotina TAFA250, localize o registro que apresenta a inconsistência e selecione o botão **"Alterar"**;

6. Como o registro aberto para edição, entre na aba **"Demonstrativos de Valores"**.

7. Posicione em cada um dos demonstrativos de valores, a fim de localizar a lotação/estabelecimento que não possui o Grau de Exposição a Agentes Nocivos preenchidos.

8. Localizado o Estabelecimento/Lotação (lembrando de consultar as remunerações em períodos anteriores), navegue até o grupo **"Informações da Remuneração do Trabalhador no Período de Apuração"**;

9. Localize o campo na coluna **"Grau de Expos."**, que estará sem conteúdo, preencha para que não ocorra mais a inconsistência, ao tentar transmitir.

Exemplo em período de apuração:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11074428572823)

Exemplo em períodos anteriores:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11074568207127)

10. Realizado o preenchimento do campo Grau Expos., salve, e retransmita o evento.
