---
article_id: 360007452371
category: Contabilidade Gerencial - Reprocessamento
content_hash: 7aba7f1899ad0db29d1e516bd5b9209b0757da5627d1b6782ee477481d21000f
fetched_at: '2026-06-28T22:40:41.892022+00:00'
product: protheus
section_id: 1500001548742
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - Como realizar o reprocessamento
  de saldos no SIGACTB
type: support-article
updated_at: '2026-02-09T20:41:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007452371-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Como-realizar-o-reprocessamento-de-saldos-no-SIGACTB
---

**Dúvida**  
Como realizar o reprocessamento de saldos ?

**Ambiente**  
Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial - a partir da versão 12.1.2410

**Solução**

O reprocessamento de saldos, tem o objetivo de recalcular os saldos de entidades contábeis, em um determinado período. Esses saldos serão recalculados, sempre, a partir dos lançamentos contábeis. Os saldos contábeis são gravados diariamente.

O sistema refaz os saldos básicos e compostos de:

* Contas Contábeis
* Centros de Custo
* Itens Contábeis
* Classes de Valor
* Totais de Lote e Documentos

O reprocessamento deve ser utilizado caso ocorram problemas com os saldos contábeis, ocasionados por:

* Saldos de Balancete e Razão diferentes;
* Importação de lançamentos por rotinas externas do sistema;
* Restauração de *backups*.

Parâmetros Utilizados

* [**MV\_ATUSAL**](https://tdn.totvs.com/display/public/PROT/SIGACTB+-+Diversos+--+24238) - Define se atualiza, ou não, saldos contábeis básicos durante o lançamento.
* [**MV\_CTBCUBE**](https://tdn.totvs.com/pages/viewpage.action?pageId=338368502)- Cubo contábil (Estando ativado irá verificar as tabelas CVX e CVY)

  "0" -> Desligado | "1"-> Ligado.   
  Este parâmetro tem influência direta no desempenho, porem a utilização deste depende do negócio, visto que é responsável pelo controle de saldos entre as entidades adicionais.

  Saiba mais sobre os parâmetros contábeis:

<http://tdn.totvs.com/display/PROT/SIGACTB+-+Diversos+--+24238>

[Cross Segmento - Backoffice Linha Protheus - SIGACTB PARÂMETROS CONTÁBEIS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052504474-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-PAR%C3%82METROS-CONT%C3%81BEIS)

Para executar o Reprocessamento temos duas formas:

1° Ajuste de saldos através da rotina Fechamento Contábil (CTBA960), a rotina possui a opção de ajuste de saldo conforme a documentação:

[*Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA960 - Processo de atualização de saldos.*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/36347421005975-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA960-Processo-de-atualiza%C3%A7%C3%A3o-de-saldos)

2° Ajuste de saldos de Forma atemática através da rotina Correção de Saldos Automáticos (CTBA980), esta rotina realiza o ajuste dos saldos de forma automática através do agendamento via Schedule conforme a documentação:

[Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA980 - Correção automática de Saldos.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/36323009088791-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA980-Corre%C3%A7%C3%A3o-autom%C3%A1tica-de-Saldos)

**Veja Mais**

* [Cross Segmento - Backoffice Linha Protheus - SIGACTB - Reprocessamento de Saldos em Fila (CTBA193)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006706472)
* [Cross Segmento - Backoffice Linha Protheus - SIGACTB - Reprocessamento não atualiza saldos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006689012)
* [Correção automática de Saldos (CTBA980) - Linha Microsiga Protheus - TDN](https://tdn.totvs.com/pages/releaseview.action?pageId=851295422&searchId=L9A7D3ETG)
* [Fechamento Contábil (SIGACTB) - Linha Microsiga Protheus - TDN](https://tdn.totvs.com/pages/releaseview.action?pageId=722662924)
