---
content_hash: d9420aaa1935ab3ec9f102117a41d80c3c1f9393b2f80d39a521d1e7d38afdd0
fetched_at: '2026-06-29T00:10:38.649815+00:00'
page_id: '544709064'
product: rm
source: tdn-rm
title: Testes comparativos do TDE no Oracle
type: documentation
url: https://tdn.totvs.com/display/LRM/Testes+comparativos+do+TDE+no+Oracle
version: 21
---

Para realização dos testes comparativos utilizamos as 3 versões do Oracle atualmente homologadas para o RM, sendo essas: 11g, 12c e 18c.

## Resultados

##### Conversão da base de dados EXEMPLO da versão 12.1.22 para a versão 12.1.28:

##### Geração de Espelho de Ponto (PtoProcRelatEspelhoCartao)

##### Solicitação de recálculo da folha de ponto (PtoProcCalculo)

## **Testes com relatório AWR**

Para os testes utilizamos relatório Automatic Workload Repository (AWR), para versão do **Oracle 11g** (11.2.0.1.0) ao qual apuramos os valores de uso em estatísticas de memória, cache e estatisticas de conjunto compartilhado com e sem o recurso de TDE habilitado, abaixo estão os quadros para comparação:

### Estatísticas de memória

                                                       **COM TDE                                                                                       SEM TDE**

   

### Tamanhos de Cache

                                                       **COM TDE                                                                                       SEM TDE**

### Estatísticas de conjunto compartilhado

                                                       **COM TDE                                                                                       SEM TDE**

Em nossos testes concluímos que a utilização do TDE apresentou um aumento no uso de memória SGA e PGA, aumento em processamento CPU e redução de I/O. Contudo,  houve um ganho de performance em relação aos tempos nas ações de recálculo do espelho do ponto, geração do relatório do espelho do ponto e conversão da base de dados pelo Atualizador. 

**Observação:**

Precisamos reforçar que este ganho de performance foi mapeado somente nestes itens aqui citados, cabe ao cliente criar seu laboratório (TDE) utilizando a documentação da Oracle e coletar os tempos de suas rotinas com e sem o recurso antes de aplica-lo em produção.

Orientações e mais detalhes sobre o TDE estão detalhadas no Help Center da Oracle:

<https://docs.oracle.com/database/121/ASOAG/introduction-to-transparent-data-encryption.htm#ASOAG10117>

Documentação da Oracle com mais dúvidas e demais detalhes sobre o relatório AWR estão contidos no Help Center da Oracle:

<https://docs.oracle.com/cd/E11882_01/server.112/e41573/autostat.htm#PFGRF027>

Não percebemos qualquer incompatibilidade na utilização do TDE com as bases de dados RM.
