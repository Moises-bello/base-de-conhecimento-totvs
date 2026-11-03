---
content_hash: 826312bd2b9c519af2b460d2e5c0ad82e1883c058fd67325d6648f2446770723
fetched_at: '2026-06-29T00:11:15.730306+00:00'
page_id: '662417764'
product: rm
source: tdn-rm
title: Nota Técnica nº 23/2021 - Leiaute 2.5
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=662417764
version: 11
---

false

**A partir dos patches:**

* 12.1.32.244
* 12.1.33.183
* 12.1.34.102
* e Superiores.

### **Objetivo:**

Em 30/12/2021 foi disponibilizado pelo eSocial a [Nota Técnica 23/2021](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/nota-tecnica-23-2021.pdf), apontando ajustes no Leiaute 2.5.

Seguem orientações referente ao produto TOTVS Folha de Pagamento para atender essa alteração:

11AtualizadorAtualizador

Após a liberação da versão será necessário executar os script's de adequação das tabelas e campos do sistema através do sistema **RM.Atualizador.exe.**

true2AlteraçõesAlterações

1) Disponibilizado no parametrizador a nova descrição do leiaute, conforme abaixo:

2) Evento S-1005: Retirada a condição do Grupo {infoObra}, para que o grupo seja informado independentemente do indicativo de desoneração da folha, conforme abaixo:

| DE | PARA |
| --- | --- |
| O (se indConstr em S-1000 = [1], indDesFolha em S-1000 = [1] e ideEstab/tpInsc = [4]);  N (nos demais casos) | O (se indConstr em S-1000 = [1] e ideEstab/tpInsc = [4]);  N (nos demais casos) |

Ajuste na tela do Empregador:

3) Melhoria da redação dos códigos de categoria relativos a médico residente ou residente em área profissional de saúde e a bolsa, conforme abaixo:

| DE | PARA |
| --- | --- |
| 902 - Médico Residente 903 - Bolsista, nos termos da lei 8958/1994 | 902 - Médico residente ou residente em área profissional de saúde |
| 903 - Bolsista, nos termos da lei 8958/1994 | 903 - Bolsista |

 

Ajuste na categoria demonstrada no cadastro do funcionário:

4) Tabela - Natureza das Rubricas da Folha de Pagamento, alterado o nome e descrição da natureza de código [9231], conforme abaixo:

| DE | PARA |
| --- | --- |
| Valor correspondente ao desconto referente a mensalidade sindical do trabalhador | Valor correspondente ao desconto referente a mensalidade sindical ou associativa do trabalhador |

5) S-2210 - Comunicação de Acidente de Trabalho, ajuste na validação da tag <hrAcid > para contemplar o acidente de trajeto, conforme abaixo:

| DE | PARA |
| --- | --- |
| Validação: Preenchimento obrigatório e exclusivo se tpAcid = [1]. Se informada, deve estar no intervalo entre [0000] e [2359], criticando inclusive a segunda parte do número, que indica os minutos, que deve ser menor ou igual a 59. | Validação: Preenchimento obrigatório e exclusivo se tpAcid = [1, **3**]. Se informada, deve estar no intervalo entre [0000] e [2359], criticando inclusive a segunda parte do número, que indica os minutos, que deve ser menor ou igual a 59. |

Geração do XML:
