---
article_id: 4402890049559
category: Contabilidade Gerencial - Movimentos, Lançamentos contábeis automáticos,
  lançamentos manuais e contabilização
content_hash: 5dd41665d5a4a9a850c9552f9e4fa39456fbf60527cd6d9e434b2873df31b9a8
fetched_at: '2026-06-28T22:40:32.567012+00:00'
product: protheus
section_id: 1500001537961
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBA105 - Integração
  Contábil, Controle de Transação - MV_TTS
type: support-article
updated_at: '2022-11-23T12:20:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402890049559-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA105-Integra%C3%A7%C3%A3o-Cont%C3%A1bil-Controle-de-Transa%C3%A7%C3%A3o-MV-TTS
---

**Dúvida**Integração Contábil Controle de Transação - MV\_TTS

**Ambiente**Cross Segmento - Backoffice Linha Protheus – Contabilidade Gerencial – A partir da versão 12.  
  
**Solução**

## O controle de transação (MV\_TTS) é uma ferramenta importante que garante a integridade de dados quando uma determinada operação é realizada no Banco de Dados. As alternativas existentes quando da atualização de tabelas são :

* Efetivar a transação - quando realizada com sucesso
* Voltar a status anterior (rollback) - desfaz toda a transação iniciada quando o final da transação não foi concluído com sucesso. Isto garante a total integridade dos dados.

O Protheus possui o parâmetro MV\_TTS que quando ativado garante que este processo exista nos processos críticos de transação de arquivos.  
  
A mensagem "Transaction Mode is in off Mode" na carga do sistema indica que o parâmetro está desativado. Esta mensagem não influencia em nada a utilização do somente, porem indica que o Banco de Dados não possui a garantia do controle de transação.  
  
A Microsiga recomenda sempre que este controle esteja ativado, pois caso o mesmo não esteja e se a estação vier a "cair" por qualquer motivo e o sistema estiver efetuando atualizações de arquivos o mesmo será interrompido e o controle de transação não irá "desfazer" toda a transação (roll back).  
  
Em relação ao questionamento sobre o fato de se ter contabilização one line, a Microsiga indica algumas sugestões :  
  
Não é recomendado o controle transacional em processos longos (Ex. Geração de Notas Fiscais e contabilização on line). O fato se deve basicamente a 2 fatores :

* O processo longo poderá gerar um grande numero de locks simultâneos no Banco de Dados, fazendo com que o processo de atualização no Banco (Commit) degrade a performance do mesmo e possa "segurar" alguns registros para outro usuário.
* Não recomendamos o uso de interface "durante" a transação (intervalo entre BEGIN Transaction e End Transaction) pois o fato de existir a interação com o usuário irá segurar todos os locks pendentes até a efetivação dos registros no Bancos de Dados por um tempo mais longo (lembre-se de que neste caso dependemos da confirmação do usuário).

Para solucionar o "problema" sugerimos que a contabilização das notas de entrada e saidas sejam efetuadas de forma off line em pequenos períodos (Ex. 1 dia).  
  
Para processos curtos com transação (Ex. Implantação de Títulos), apesar de existir a interface, a interferência será mínima pois o numero de locks pendentes é controlado e normalmente pequeno, pois a contabilização é individual.  
  
Em suma, apesar de todos pros e contras, sem duvidas, o controle transacional é uma forte ferramenta para mantermos a base de dados de nossos clientes intactas.

Saiba mais

<https://tdn.totvs.com/pages/releaseview.action?pageId=6814812>
