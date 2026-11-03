---
content_hash: 0b6f1581441e5a62b2a38b9e607b7f7f685941c74bcfeadbaf45de79759380e2
fetched_at: '2026-06-29T00:08:12.193975+00:00'
page_id: '243638378'
product: rm
source: tdn-rm
title: TUHCZN_DT_IRRF_De_Ferias_Funcionario_Transferido
type: documentation
url: https://tdn.totvs.com/display/LRM/TUHCZN_DT_IRRF_De_Ferias_Funcionario_Transferido
version: 122
---

# RESCISÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Transferência de Funcionário* |
| **Situação/Requisito:** | Na competência 11/2015, usuário cadastrou férias para o funcionário de 01/12/2015 à 30/12/2015. Após cadastrado das férias e calcular, foi realizada a transferência do funcionário para outra seção da mesma coligada com a data de 30/11/2015. Após liberação da competência para 12/2015, na seção atual do funcionário foi processada o cálculo das férias com a data de pagamento em 27/11/2015. Ao gerar o arquivo da DIRF 2015, os valores referentes as férias não são informadas devido a data de pagamento. Cliente solicita que o sistema emita uma mensagem de aviso, informando que caso a transferência seja efetuada com a data posterior ao pagamento das férias, o valor não será levado para geração da DIRF. |
| **Solução/Implementação:** | *No momento da rescisão por transferência foi adicionado uma validação que impede que tenha alguma férias marcadas com data de pagamento anterior a data da transferência.* |
| **Chamados relacionados:** | *TUHCZN, TVEJOA* |

divs
