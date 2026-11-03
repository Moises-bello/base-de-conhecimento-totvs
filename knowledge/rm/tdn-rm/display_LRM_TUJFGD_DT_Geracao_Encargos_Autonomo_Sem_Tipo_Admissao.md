---
content_hash: 2037765b2115da045d9e4b5590df57e8884ac9ce7bb035a7bac9e384bea866e5
fetched_at: '2026-06-29T00:06:30.276799+00:00'
page_id: '235318223'
product: rm
source: tdn-rm
title: TUJFGD_DT_Geracao_Encargos_Autonomo_Sem_Tipo_Admissao
type: documentation
url: https://tdn.totvs.com/display/LRM/TUJFGD_DT_Geracao_Encargos_Autonomo_Sem_Tipo_Admissao
version: 2
---

# GERAÇÃO DE ENCARGOS NÃO PROCESSA AUTONOMO SEM O TIPO DE ADMISSÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Geração de Encargos* |
| **Situação/Requisito:** | *Não está gerando encargo por fórmula para funcionário Autônomo, sem o preenchimento da informação do Tipo de Admissão no cadastro do funcionário.*  *Ao final do processo apenas exibe a mensagem: "Início do processamento dos encargos de 0 funcionário(s)".* |
| **Solução/Implementação:** | *Ajuste na geração de encargo por fórmula, para permitir o processamento de funcionário Autônomo, que não tem a informação do Tipo de Admissão no cadastro.*  *Este tipo de consistência não é necessário neste módulo, no caso de Autônomos.* |
| **Chamados   relacionados:** | *TUJFGD, TUOKT3* |
| **Versões/Release:** | *11.82.43, 12.1.11* |
