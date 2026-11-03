---
content_hash: ae0b175069b9f0d5b93727144e1342db4e8ddf2b2afe68e5c4b289df3d706467
fetched_at: '2026-06-29T00:11:15.679452+00:00'
page_id: '661613517'
product: rm
source: tdn-rm
title: Nota Técnica nº 04/2021 - Leiaute S-1.0
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=661613517
version: 35
---

# Objetivo

Em 30/12/2021 foi disponibilizado pelo eSocial a [Nota Técnica 04/2021](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/nota-tecnica-s-1-0-04-2021.pdf), apontando ajustes no Leiaute S-1.0.

Seguem orientações referente ao produto TOTVS Folha de Pagamento para atender essa alteração:

11AtualizadorAtualizador

Após a liberação da versão será necessário executar os script's de adequação das tabelas e campos do sistema através do sistema **RM.Atualizador.exe.**

true2AlteraçõesAlteraçõesfalse

**A partir dos patches:**

* 12.1.32.244
* 12.1.33.183
* 12.1.34.102
* e Superiores.

1) Disponibilizado no parametrizador a nova descrição do leiaute, conforme abaixo:

2) Evento S-1005 -Tabela de Estabelecimentos, Obras ou Unidades de Órgãos Públicos, retirada a condição do Grupo {infoObra}, para que o grupo seja informado independentemente do indicativo de desoneração da folha, conforme abaixo:

| DE | PARA |
| --- | --- |
| O (se indConstr em S-1000 = [1], indDesFolha em S-1000 = [1] e ideEstab/tpInsc = [4]);  N (nos demais casos) | O (se indConstr em S-1000 = [1] e ideEstab/tpInsc = [4]);  N (nos demais casos) |

Ajuste na tela do Empregador, conforme destacado abaixo:

3) Categoria eSocial, melhoria na redação dos códigos de categoria relativos a médico residente ou residente em área profissional de saúde e a bolsa, conforme abaixo:

| DE | PARA |
| --- | --- |
| 902 - Médico Residente 903 - Bolsista, nos termos da lei 8958/1994 | 902 - Médico residente ou residente em área profissional de saúde |
| 903 - Bolsista, nos termos da lei 8958/1994 | 903 - Bolsista |

 

4) Tabela 03 - Natureza das Rubricas da Folha de Pagamento, alterada a descrição da natureza do código [9231], conforme abaixo:

| DE | PARA |
| --- | --- |
| Valor correspondente ao desconto referente a mensalidade sindical do trabalhador | Valor correspondente ao desconto referente a mensalidade sindical ou associativa do trabalhador |

5) Tabela 25 - Tipos de Benefícios, inserido os registros abaixo no campo "Tipo do benefício" na tela de dados do benefício do anexo do funcionário.

6) Evento S-2210 - Comunicação de Acidente de Trabalho, ajuste na validação da tag <hrAcid > para contemplar o acidente de trajeto, conforme abaixo:

| DE | PARA |
| --- | --- |
| Validação: Preenchimento obrigatório e exclusivo se tpAcid = [1].  Se informada, deve estar no intervalo entre [0000] e [2359], criticando inclusive a segunda parte do número, que indica os minutos, que deve ser menor ou igual a 59. | Validação: Preenchimento obrigatório e exclusivo se tpAcid = [1, **3**].  Se informada, deve estar no intervalo entre [0000] e [2359], criticando inclusive a segunda parte do número, que indica os minutos, que deve ser menor ou igual a 59. |

Geração do XML:

 

7) Evento S-2206 - Alteração de Contrato de Trabalho/Relação Estatutária, correção na ocorrência e condição do grupo <infoRegimeTrab>, por não haver informação a ser prestada para servidor estatutário vinculado a RGPS, conforme abaixo:

| DE | PARA |
| --- | --- |
| O (se tpRegTrab em S-2200 = [1]); N (nos demais casos) | N (se tpRegPrev = [1] e tpRegTrab em S-2200 = [2]); O (nos demais casos) |

Geração do XML do evento S-2200:

Geração do XML do evento S-2206: o grupo {infoRegimeTrab} não foi gerado:

true3Alterações - Parte 2Alterações - Parte 2false

**A partir dos patches:**

* 12.1.32.267
* 12.1.33.224
* 12.1.34.134
* e Superiores.

1) Disponibilizado no parametrizador a nova descrição do leiaute, conforme abaixo:

2) Evento S-1000: acrescentado campo  dtTrans11096

Ajuste na tela do Empregador:

3) Evento S-1005: acrescentado campo cnpjResp no xml

 

Este campo será gerado quando o ideEstab/tpinsc = 4 e levará o campo CGCCFO do cliente/fornecedor

4) S-1005: Alterada validação do campo FAP conforme abaixo:

DE:

PARA:

5) S-1280: Incluído novo grupo no evento

6) S-1299:Incluído o campo no cadastro de período de apuração.

7)S-2300 : Grupo {infoTrabCedido} – alteradas descrição e condição

DE:

PARA:

8) S-2300: Campo {infoTrabCedido/tpRegPrev} – alterada validação

DE:

PARA:

9) S-2300: Campos (Categoria de origem do servidor, CNPJ do orgão publico de origem, matricula do servidor no orgão publico de origem, data de exercicio do servidor orgão publico de origem) criados na aba de estatutário para mandato eletivo (categoria 304) e no histórico de estatutário.
