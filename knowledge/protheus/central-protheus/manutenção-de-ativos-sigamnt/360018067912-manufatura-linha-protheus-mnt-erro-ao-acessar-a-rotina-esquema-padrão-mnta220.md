---
article_id: 360018067912
category: Manutenção de Ativos (SIGAMNT)
content_hash: 8d098b8d45bbb6d1573b91f4a99ae0a2d3928e94e76feef8c30b80d0c6267315
fetched_at: '2026-06-28T22:42:33.158282+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Erro ao Acessar a Rotina Esquema Padrão
  MNTA220
type: support-article
updated_at: '2021-08-24T17:00:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018067912-Manufatura-Linha-Protheus-MNT-Erro-ao-Acessar-a-Rotina-Esquema-Padr%C3%A3o-MNTA220
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:00 min****Ocorrência**No módulo **Manutenção de Ativos**, ao acessar a rotina **MNTA220 - Esquema Padrão**, é apresentada a mensagem **Foi identificado um problema no índice único das Tabela TQ0 ou TQ1, Dessa forma o parâmetro MV\_NGMNTFR (Utiliza frota) será considerado como N-Não utiliza. Favor entrar em contato com o administrador do Sistema.**  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Todas as versões  
  
**Causa**A mensagem ocorre por erro ou falta de configuração do campo **X2\_UNICO** das tabelas **TQ0 - Desenho do Rodado** e **TQ1 - Itens do Desenho do Rodado    
  
Solução**Para solucionar essa ocorrência em releases anteriores a **12.1.33 - Harpia**:

* Configure no **ini**do **AppServer** a chave:  

  ```
  [General]  
  UPDNGMNTFR=1
  ```
* E altere o **X2\_UNICO** das tabelas **TQ0** e **TQ1** para:  
  **TQ1: TQ1\_FILIAL+TQ1\_DESENH+TQ1\_TIPMOD+TQ1\_SEQREL**  
  **TQ0: TQ0\_FILIAL+TQ0\_DESENH+TQ0\_TIPMOD**

Para releases **12.1.33 - Harpia** e posteriores, as chaves únicas já estão ajustadas.
