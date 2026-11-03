---
content_hash: 8ab0b51a234e5aceec425a84decf72726b7ec269aebd72a6750b53090f41943f
fetched_at: '2026-06-29T00:08:34.891280+00:00'
page_id: '274850766'
product: rm
source: tdn-rm
title: 931593 FOPROTINAS01-505 INTEGRACAO LANCAMENTOS CONTABEIS COM MAIS DE 999 PARTIDAS
type: documentation
url: https://tdn.totvs.com/display/LRM/931593+FOPROTINAS01-505+INTEGRACAO+LANCAMENTOS+CONTABEIS+COM+MAIS+DE+999+PARTIDAS
version: 107
---

# LANÇAMENTOS CONTÁBEIS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Lançamentos Contábeis |
| **Situação/Requisito:** | Ao gerar lançamento contábil com mais de 1000 partidas ocorre um erro ao integrar com o Protheus, pois o campo de número da linha possui apenas 3 caracteres e não é possível utilizar letras pois o adapter do protheus sempre tenta converter para inteiro. |
| **Solução/Implementação:** | Foi criado um parâmetro no parâmetrizador do Labore, acessando o item "06.02 - Integrações", "06.02.06 - Outros Backoffice"      Em seguida habilite o parâmetro:      Dessa forma, ao integrar um lançamento contábil com o Protheus, o número das partidas será enviado em branco e será gerado automaticamente pelo Protheus, seguindo a lógica utilizada ao cadastrar um lançamento manualmente.    **Atenção:** é necessário que o Protheus já esteja na versão mais recente de forma que saiba tratar essa particularidade. Caso o Protheus tente inserir todas as partidas com o número de Linha 000 será necessário atualizar a versão. |
| **Tickets relacionados:** | 931593 |

divs
