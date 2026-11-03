---
content_hash: bc0eb114332e83d9733b7d6b8ca2d9f3c683ac4638356b5ce135c34947ed8f47
fetched_at: '2026-06-29T00:06:23.552071+00:00'
page_id: '224105841'
product: rm
source: tdn-rm
title: TUAUAZ_DT_Deducao_Dependente_Decimo_Terceiro_Base_Negativa
type: documentation
url: https://tdn.totvs.com/display/LRM/TUAUAZ_DT_Deducao_Dependente_Decimo_Terceiro_Base_Negativa
version: 124
---

# DIRF/INFORME DE RENDIMENTOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *DIRF/Informe de Rendimentos* |
| **Situação/Requisito:** | *1 -* Ao gerar a Dirf em arquivo para funcionário com rescisão complementar por dissidio (RRA) com valor de ano anterior, sistema está levando a dedução de dependente, sem informar a base de IRRF.  2 - Ao gerar a Dirf em arquivo, para funcionário com base de 13º negativa, sistema leva valor de dedução de dependentes.  3 - Ao utilizar a opção Lançar Valores para o Gerador de Relatórios e Informe de Rendimentos em TXT o sistema não está atualizando os dados da PDIRF. |
| **Solução/Implementação:** | *1 - Ajustado validação se tem base de irrf quando o funcionário tem RRA;*  *2 - Ajustado validação da base de irrf de 13º para considerar se deve informar a dedução de dependente ou não;*  *3 - Tratado as situações que impediam o sistema de lançar os valores para o gerador de relatórios quando utilizava o informe de rendimentos em txt.*  *4 - Criado opção para o usuário lançar apenas os valores para o gerador de relatório fazendo com que a geração seja mais rápida. Antes o sistema sempre gerava o informe de rendimentos, mesmo quando o usuário não ia utilizar.* |
| **Chamados relacionados:** | TUAUAZ,TUBBSE, TUBPIM, TUBTF8, TUBTFG, TUBTJF, TUBTL3 |
| **Versões/Release:** | *11.82.42,11.83.55, 12.1.8 e 12.1.9* |

divs
