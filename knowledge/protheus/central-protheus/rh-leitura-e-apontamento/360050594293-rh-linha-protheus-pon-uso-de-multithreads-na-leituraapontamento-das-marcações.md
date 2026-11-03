---
article_id: 360050594293
category: RH - Leitura e Apontamento
content_hash: 5d18fd03508f782d67425c5cf79044a553825243874ae2a1ebd35355eb467734
fetched_at: '2026-06-28T22:44:46.030251+00:00'
product: protheus
section_id: 32419281460119
source: central-protheus
title: RH - Linha Protheus - PON - Uso de Multithreads na Leitura/Apontamento das
  marcações
type: support-article
updated_at: '2025-10-13T16:37:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050594293-RH-Linha-Protheus-PON-Uso-de-Multithreads-na-Leitura-Apontamento-das-marca%C3%A7%C3%B5es
---

****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35599153084311) Tempo aproximado para leitura: 00:01:00 min**Dúvida**Como usar ***Multithreads*** na **Leitura/Apontamento das marcações?**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**Com a criação do parâmetro **MV\_PONMULT**, ao efetuar a **Leitura/Apontamento** das marcações, o produto permite definir a utilização de ***Multi-Threads*** em sua execução, melhorando assim a performance da rotina.  
  
Para configurar, acesse o **Configurador > Ambiente > Cadastros > Parâmetros** e localize o **MV\_PONMULT:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19151464920343)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19151464944919)  
  
Quanto a **utilização** e **quantidade** de *threads* utilizadas:   
- O departamento de **Infraestrutura/T.I. da empresa** deve **analisar criteriosamente a necessidade  interna da empresa para tal definição;**- A quantidade máxima de *threads* varia de servidor para servidor, por este motivo, antes de implementar, sugerimos a realização de testes:

**Exemplo:**Adicionar sempre **1 *thread*** por vez. Teste a leitura com 2 *threads* ativas **(MV\_PONMULT = 2)**, e verifique se o tempo de execução da Leitura (performance) diminui. Caso tenha diminuído, teste novamente com 3 *threads* ativas e verifique a performance.  
Caso o tempo de execução aumente com 3 *threads*, então a quantidade ideal será de apenas 2 *threads*, caso contrário aumente as *threads* para 4 e veja o resultado, até encontrar a quantidade ideal para o seu servidor.   
  
A utilização de **muitas *threads* em um servidor que não suporta a carga de processamento** pode  gerar efeito contrário, deixando o **processo mais lento.**   
  
**Saiba Mais:**[Manual do Ponto](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373) [Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua - Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854)
