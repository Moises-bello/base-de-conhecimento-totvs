---
article_id: 20806195579799
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 306c80a33a94df947e8056d38daacb357b07b39cafe2b7a698bd729fcfe046b6
fetched_at: '2026-06-28T22:37:55.402944+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA150 - Como gerar
  o Nosso Número no Arquivo de remessa sem os zeros a esquerda
type: support-article
updated_at: '2024-01-24T17:12:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20806195579799-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA150-Como-gerar-o-Nosso-N%C3%BAmero-no-Arquivo-de-remessa-sem-os-zeros-a-esquerda
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20806195522839) Tempo aproximado para leitura: **00:10:00 min****Dúvida**É possível gerar o Nosso número no Arquivo de remessa (FINA150) sem os zeros a esquerda?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**O **Parâmetros de bancos (FINA130)** por padrão tem 12 caracteres que podem gerar a numeração iniciando com zeros, exemplo: **000059090007**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20806195524375)  
  
Porém, supomos que o banco aceita apenas 8 caracteres, onde pode gerar nesse formato a rejeição do banco  
  
Para não gerar os zeros no arquivo de remessa para o banco, deve usar a função **[SUBSTR()](https://tdn.totvs.com/display/tec/SubStr)**  
**Exemplo:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20806195528855)  
  
No exemplo acima usamos a função **SubStr** passando a função do **NossoNum**, em seguida informamos em qual posição irá iniciar que será a partir da 5 posição e quanto caracteres retiraremos parte da **String**, que será 8.   
  
Ao gerar o **arquivo de remessa**, será gerado o **Nosso número** da seguinte maneira, sem os zeros a esquerda, iniciando da posição 5 até a 12 = 8 caracteres  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20806195531159)

**Saiba mais**

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Principais configurações e dúvidas para uso do CNAB](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7778595184407-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Principais-configura%C3%A7%C3%B5es-e-d%C3%BAvidas-para-uso-do-CNAB)
