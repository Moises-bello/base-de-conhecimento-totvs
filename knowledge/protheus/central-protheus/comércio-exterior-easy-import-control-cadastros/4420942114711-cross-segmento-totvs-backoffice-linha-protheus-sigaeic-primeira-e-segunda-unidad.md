---
article_id: 4420942114711
category: Comércio Exterior - Easy Import Control - Cadastros
content_hash: 0a4001581e12564e8fd047d85cf319a05170579192cf58aa0dd7079648112539
fetched_at: '2026-06-28T22:39:52.233950+00:00'
product: protheus
section_id: 1500001549382
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Primeira e segunda
  unidade de medida no SIGAEIC
type: support-article
updated_at: '2022-07-14T12:07:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4420942114711-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Primeira-e-segunda-unidade-de-medida-no-SIGAEIC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como configurar a segunda unidade de medida no SIGAEIC?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - *Easy Import Control* - Todas as versões  
  
**Solução**No *Easy Import Control* (SIGAEIC) o sistema permite através de parametrização fazer a manutenção do processo de importação com base na unidade de compra do produto nos casos em que esta é diferente da unidade produtiva do mesmo.  
Para tanto, é necessário definir no cadastro do produto importado a primeira unidade de medida (geralmente a unidade produtiva) e a segunda unidade de medida (geralmente a unidade de compra).  
É preciso definir também no parâmetro MV\_UNIDCOM qual será a unidade (primeira ou segunda) adotada pelo SIGAEIC para controle destas informações.![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4420949630871/mceclip0.png)  
  
É preciso definir também no parâmetro **MV\_UNIDCOM** qual será a unidade (primeira ou segunda) adotada pelo SIGAEIC para controle destas informações.  
Utilizando o parâmetro MV\_UNIDCOM = 2, deve seguir o procedimento, para que o processo no SIGAEIC, seja calculado com a segunda unidade de medida:  
1. Criar uma SC no módulo de Compras (SIGACOM), utilizando um produto que tenha a segunda unidade de medida.   
2. A partir da SC, gerar a SI;  
3. No SIGAEIC, incluir um PO para esta SI e Desembaraço.   
  
**Saiba mais**  
[Primeira e segunda unidade de medida no SIGAEIC](https://tdn.totvs.com/display/public/PROT/Primeira+e+segunda+unidade+de+medida+no+SIGAEIC)
