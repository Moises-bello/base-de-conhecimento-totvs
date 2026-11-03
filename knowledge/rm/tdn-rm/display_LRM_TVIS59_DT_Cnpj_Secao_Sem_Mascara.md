---
content_hash: c056b9202b9e98f1dbf92b1b1f025ae97baabe06427b98c1ef844ba910487456
fetched_at: '2026-06-29T00:08:14.303226+00:00'
page_id: '244448928'
product: rm
source: tdn-rm
title: TVIS59_DT_Cnpj_Secao_Sem_Mascara
type: documentation
url: https://tdn.totvs.com/display/LRM/TVIS59_DT_Cnpj_Secao_Sem_Mascara
version: 112
---

# SEÇÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Cadastro de Seção* |
| **Situação/Requisito:** | As seções do cliente estão com o CNPJ informado sem máscara, ao tentar incluir uma nova seção ou alterar o CNPJ da seção informando a máscara o sistema apresenta o seguinte erro.  {0} ({1}) incompatível com o básico do CNPJ da seção superior a esta (seção principal, CNPJ básico: {2} ) |
| **Solução/Implementação:** | *Ajustado mensagem ao alterar o código da seção quando a raiz do cnpj da seção não é igual ao cnpj da coligada.* |
| **Chamados relacionados:** | *TVIS59* |

divs
