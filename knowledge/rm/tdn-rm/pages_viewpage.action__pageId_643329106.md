---
content_hash: 5baf0aef543dbb95387e546a0f5d1ee619232b9ff2240757a09b0777945d6482
fetched_at: '2026-06-29T00:11:10.343154+00:00'
page_id: '643329106'
product: rm
source: tdn-rm
title: Nota Técnica nº 03/2021
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=643329106
version: 15
---

false

**A partir dos patches:**

* 12.1.31.247
* 12.1.32.187
* 12.1.33.114
* e Superiores.

Objetivo:

[Em 31/08/2021 foi disponibilizado pelo eSocial a Nota Técnica, apontando ajustes no Layout S](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/nota-tecnica-s-1-0-03-2021.pdf)-1.0.

1Seguem orientações referente ao produto TOTVS Folha de Pagamento, para atender essa alteração:1AtualizadorAtualizador

Após a liberação da versão será necessário executar os script's de adequação das tabelas e campos do sistema através do sistema **RM.Atualizador.exe.**

true2AlteraçõesAlterações

1)Disponiblizado no parametrizador o layout.

2) Tabela 18 - incluídos códigos de motivo de afastamento [39, 40].

Incluído os motivos 39 e 40 no DE/PARA de afastamento para serem utilizados no evento S-2230.

3) S-1005: Grupos {infoObra} – alteradas condição e descrição no registro do evento.

DE: O (se indConstr em S-1000 = [1]e ideEstab/tpInsc = [4]); N (nos demais casos)

PARA: O (se indConstr em S-1000 = [1], indDesFolha em S-1000 = [1] e ideEstab/tpInsc = [4]); N (nos demais casos)

**Observação**: Este grupo é impresso somente quando utiliza tomador de serviço.

4)S-1200:  Grupos {infoAgNocivo} – alterada condição.

DE: O (se codCateg = [1XX, 2XX, 3XX, 731, 734, 738]); N (nos demais casos)

PARA: O (se codCateg = [1XX, 2XX, 3XX,731, 734, 738] ou se codCateg = [4XX] com {categOrig} em S-2300 = [1XX, 2XX, 3XX, 731, 734, 738]); N (nos demais casos)

5) S-1299: Campo {transDCTFWeb} – alterada validação.

DE: Preenchimento obrigatório se classTrib em S-1000 = [04] ou indGuia estiver informado.

PARA: Não informar se perApur < [2021-10]. Preenchimento obrigatório se perApur >= [2021-10] e  
(classTrib em S-1000 = [04] ou indGuia estiver informado).

Para gerar a tag acesse o nenu RH | Folha de Pagamento | eSocial | Período de Apuração

6) S-1260: Campo {nrInscEstabRural} – alterada validação.

DE: Deve ser um número de inscrição válido e existente na Tabela de Estabelecimentos (S-1005). Se  
indGuia estiver preenchido, o número de inscrição deve possuir tpCaepf em S-1005 = [3].

PARA: Deve ser um número de inscrição válido e existente na Tabela de Estabelecimentos (S-1005).

 7) S-2210: Grupo {atestado} – alteradas ocorrência e condição

O grupo atestado se tornou obrigatório.

8) S-2210: Campos {hrAcid}, {hrsTrabAntesAcid} e {hrAtendimento} – alterado tipo.

De:

Para:

Ajuste no tipo do campo (para caractere), considerando que deve ser informado com zero(s) à esquerda quando for o caso.

9) S-2210: Campo {codSitGeradora} – alterada validação

DE: Deve ser um código válido e existente na Tabela 15 ou na Tabela 16.

PARA: Deve ser um código válido e existente na Tabela 15.

Como a tabela 16 se juntou com a tabela 15 foi ajustada a tela de CAT para que após a execução do atualizador ao selecionar um tipo de agente causador de doença mostre a tabela 15.

10) S-2220: Campo {obsProc} – incluída validação

Validação: Preenchimento obrigatório se procRealizado = [0583, 0998, 0999, 1128, 1230, 1992, 1993, 1994, 1995,  
1996, 1997, 1998, 1999, 9999].

11) S-2220: Campo {ordExame} – alterada ocorrência e incluída validação. 

Campo passou a ser obrigatório somente se procedimento realizado igual a 0281.

12) S-2240:  Grupo {epcEpi} – alteradas ocorrência e condição.

Grupo epcEpi deixou de ser obrigatório se código do agente nocivo igual a 09.01.001.

13)S-2240: Grupo {respReg} – alterada ocorrência e inserido campo {cpfResp} como chave.

O grupo respReg passa a aceitar 99 registros e o CPF do responsável não pode repetir nestes registros.

14)S-2240: Campo {tpAval} – alterada ocorrência e incluída validação.

Campo tpAval deixou de ser obrigatório se código do agente nocivo igual a 09.01.001.

15)Tabela 15 – alterado nome da tabela, desmembrada coluna "Descrição" (em colunas "Descrição" e "Aplicação") e incluído código [200072000].
