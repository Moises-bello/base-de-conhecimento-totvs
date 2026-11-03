---
article_id: 360025940474
category: RH - Cadastros
content_hash: e93d3b2813ce2250c4297de209c6a79804b3cce7169d50b87b72c74af94cb851
fetched_at: '2026-06-28T22:43:25.825688+00:00'
product: protheus
section_id: 360010781894
source: central-protheus
title: RH - Linha Protheus - GPE - Ao gerar a integração com WORD, de várias matrículas,
  é salvo apenas a última matrícula no arquivo de saída
type: support-article
updated_at: '2026-06-24T17:41:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025940474-RH-Linha-Protheus-GPE-Ao-gerar-a-integra%C3%A7%C3%A3o-com-WORD-de-v%C3%A1rias-matr%C3%ADculas-%C3%A9-salvo-apenas-a-%C3%BAltima-matr%C3%ADcula-no-arquivo-de-sa%C3%ADda
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24173237973655) Tempo aproximado para leitura: **00:01:00 min**

**Ocorrência**Ao gerar a integração com WORD, de várias matrículas, é salvo apenas a última matrícula no arquivo de saída

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Causa**Isso é devido a uma limitação tecnológica do Word

**Solução**Para gravar um arquivo com **todas** as matrículas, é necessário instalar na máquina local uma impressora virtual pdf, como o **PDFCreator** por exemplo. Após instalar, marque a impressora como Padrão nas configurações de Impressora do Windows.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26494922851607)

Deixe a pergunta **Impressão** nos parâmetros de integração com o Word com **Impressora** e envie para impressão.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26494969945111)

Ao final de **cada geração** das variáveis no arquivo, o próprio PDFCreator **abrirá uma tela** para salvar o arquivo no local especificado pelo usuário, gerando assim, **um arquivo para cada matrícula**.

**Saiba Mais**[RH - Linha Protheus - GPE - Configuração para Impressão de Documentos no Word (GPEWORD)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021565472-RH-Linha-Protheus-GPE-Configura%C3%A7%C3%A3o-para-Impress%C3%A3o-de-Documentos-no-Word-GPEWORD-?source=search)  
[RH - Linha Protheus - GPE - Variáveis que podem ser usadas na Integração com o WORD](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010260602-RH-Linha-Protheus-GPE-Vari%C3%A1veis-que-podem-ser-usadas-na-Integra%C3%A7%C3%A3o-com-o-WORD?source=search)  
[RH - Linha Protheus - GPE - Error log ao executar rotina de Integração com Word - NOFUNCW Opção não disponível no Protheus Função: U\_FOPTPPIS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012219001-RH-Linha-Protheus-GPE-Error-log-ao-executar-rotina-de-Integra%C3%A7%C3%A3o-com-Word-NOFUNCW-Op%C3%A7%C3%A3o-n%C3%A3o-dispon%C3%ADvel-no-Protheus-Fun%C3%A7%C3%A3o-U-FOPTPPIS?source=search)  
[RH - Linha Protheus - GPE - Integração com o Word apresenta mensagem: Não conseguimos encontrar seu arquivo. É possível que ele tenha sido movido, renomeado ou excluído](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052139513-RH-Linha-Protheus-GPE-Integra%C3%A7%C3%A3o-com-o-Word-apresenta-mensagem-N%C3%A3o-conseguimos-encontrar-seu-arquivo-%C3%89-poss%C3%ADvel-que-ele-tenha-sido-movido-renomeado-ou-exclu%C3%ADdo?source=search)
