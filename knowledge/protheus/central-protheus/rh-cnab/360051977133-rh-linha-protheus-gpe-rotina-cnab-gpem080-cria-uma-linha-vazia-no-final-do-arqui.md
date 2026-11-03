---
article_id: 360051977133
category: RH - CNAB
content_hash: 4af175bf826f70eecacb021ac97fd438aeef5c02b6124ead54e0702aee2d8e47
fetched_at: '2026-06-28T22:43:39.342787+00:00'
product: protheus
section_id: 360004833653
source: central-protheus
title: RH - Linha Protheus - GPE - Rotina CNAB (GPEM080) cria uma linha vazia no final
  do arquivo mesmo configurado como "Linha vazia no fim do arquivo = Não"
type: support-article
updated_at: '2025-09-19T21:57:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051977133-RH-Linha-Protheus-GPE-Rotina-CNAB-GPEM080-cria-uma-linha-vazia-no-final-do-arquivo-mesmo-configurado-como-Linha-vazia-no-fim-do-arquivo-N%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32854481451415)**Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Na geração do arquivo CNAB está criando uma linha vazia no final do arquivo, mesmo configurado como "Linha vazia no arquivo = Não".  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**Conforme análise do incidente, constatamos que a quebra de linha no final do arquivo não configura erro pois faz parte do conceito do CNAB. O erro seria se houvesse após o fim do arquivo, uma linha em branco seguida de outra quebra de linha.

No grupo de perguntas da rotina **Geração de Arquivos Líquidos - GPEM080**, selecionando a opção ***Layout** **cnab modelo 2***

![cnab_modelo_2_param_1.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360097320694)

No parâmetro das Perguntas ***linha Vazia no Fim do Arquivo = NÃO***

![linha_vazia_N_o.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360097321374)

O sistema gera 1 linha no fim do arquivo

![cnab_linha_vazia_n_o.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360099628493)

No parâmetro das Perguntas ***linha Vazia no Fim do Arquivo = SIM***

![linha_vazia_sim.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360099628653)

Desta forma o sistema gera 1 linha e um "CRLF" (enter) no fim do arquivo

![cnab_linha_vazia_sim.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360097322314)

No final de todas as linhas é obrigatório ter um enter para que o fim da linha seja reconhecido, portanto a opção de criar uma linha em branco no final permite que se tenha uma linha a mais somente com o "enter" (CRLF).

**Saiba Mais:**  
[Artigos - CNAB](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833653-RH-CNAB)
