---
content_hash: 3aa8c347420594475801996c98830dfb650762d054b20a6f71c10cfd3eeea67a
fetched_at: '2026-06-29T00:11:10.334971+00:00'
page_id: '643328959'
product: rm
source: tdn-rm
title: Nota Técnica nº 22/2021
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=643328959
version: 10
---

false

**A partir dos patches:**

* 12.1.31.247
* 12.1.32.187
* 12.1.33.114
* e Superiores.

# Objetivo:

---

Em 31/08/2021 foi disponibilizado pelo eSocial a [Nota Técnica 22/2021](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/nota-orientativa-22-2021.pdf), apontando ajustes no Layout 2.5.

---

1Seguem orientações referente ao produto TOTVS Folha de Pagamento, para atender essa alteração:1AtualizadorAtualizador

Após a liberação da versão será necessário executar os script's de adequação das tabelas e campos do sistema através do sistema **RM.Atualizador.exe.**

true2AlteraçõesAlterações

1)Disponiblizado no parametrizador o layout.

2) Tabela 18 - incluídos códigos de motivo de afastamento [39, 40].

Incluído os motivos 39 e 40 no DE/PARA de afastamento para serem utilizados no evento S-2230

3) S-1005: Grupos {infoObra} – alteradas condição e descrição no registro do evento.

DE: O (se indConstr em S-1000 = [1]e ideEstab/tpInsc = [4]); N (nos demais casos)

PARA: O (se indConstr em S-1000 = [1], indDesFolha em S-1000 = [1] e ideEstab/tpInsc = [4]); N (nos demais casos)

**Observação**: Este grupo é impresso somente quando utiliza tomador de serviço.

4) S-1200: Grupos {infoAgNocivo} – alterada condição.

DE: O (se codCateg = [1XX, 2XX, 3XX, 731, 734, 738]); N (nos demais casos)

PARA: O (se codCateg = [1XX, 2XX, 3XX,731, 734, 738] ou se codCateg = [4XX] com {categOrig} em S-2300 = [1XX, 2XX, 3XX, 731, 734, 738]); N (nos demais casos)

5)S-2399: Grupos {infoAgNocivo} – alterada condição.

DE: O (se {codCateg} for relativo a Avulso ou Cooperado filiado a cooperativa de produção [738] ou Cooperado de cooperativa de trabalho que presta serviço a empresa [731,734]) N (nos demais casos).

PARA: O (se {codCateg} for relativo a Avulso ou Cooperado filiado a cooperativa de produção [738] ou Cooperado de cooperativa de trabalho que presta serviço a empresa [731,734] ou se codCateg = [4XX] com {categOrig} em S-2300 = [2XX, 731, 734, 738]) N (nos demais casos).
