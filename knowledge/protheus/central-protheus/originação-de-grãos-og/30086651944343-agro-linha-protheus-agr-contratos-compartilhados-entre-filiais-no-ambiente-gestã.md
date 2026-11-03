---
article_id: 30086651944343
category: Originação de Grãos (OG)
content_hash: 08c3c2ea48eb027d84485faa4561daeff68406329b5a1333d9054aa79b41c7b1
fetched_at: '2026-06-28T22:45:38.850425+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Contratos Compartilhados entre filiais no ambiente
  Gestão Agroindústria - SIGAAGR
type: support-article
updated_at: '2025-05-21T20:58:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30086651944343-Agro-Linha-Protheus-AGR-Contratos-Compartilhados-entre-filiais-no-ambiente-Gest%C3%A3o-Agroind%C3%BAstria-SIGAAGR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30086651927703) Tempo aproximado para leitura: **00:02:30 min** **Dúvida**Como é realizado uma tabela de **Contratos Compartilhados entre filiais no ambiente Gestão Agroindústria - SIGAAGR**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução****Contratos Compartilhados entre filiais no ambiente Gestão Agroindústria - SIGAAGR**

|  |  |
| --- | --- |
| **Produto:** | Microsiga Protheus |
| **Versões:** | Protheus 11 e Protheus 12 |
| **Ocorrência:** | Ajustes ou inconsistências relacionadas ao compartilhamento de tabelas das rotinas do contrato |
| **Ambiente:** | SIGAAGR - Gestão de Agronegócio |
| **Conhecimento:** | O sistema Protheus permite a configuração das tabelas para acesso exclusivo ou compartilhado entre filiais.   No modulo SIGAAGR temos dois modelos de comercialização, o clássico e a nova comercialização, disponibilizada a partir da versão 12.1.23.  Dentro do modelo clássico, o compartilhamento deve ser exclusivo, pois as movimentações ocorrem através de romaneios por filial, ligados diretamente ao contrato.  Caso o compartilhamento das tabelas não obedeça essa regra, o sistema pode apresentar erro ou falhas durante a execução das rotinas.  Segue abaixo a relação das tabelas envolvidas na rotina de Contratos do modelo clássico:  **Tabelas Contrato Modelo clássico:**  NJR - Contratos NN7 - Previsão financeira NNY - Cadencias NNF - Despesas Corretores NN8 - Fixação Contrato NKA - Composição de Preços  Já o modelo da Nova Comercialização existe a possibilidade de alterar o compartilhamento das tabelas do contrato. As alterações devem ser realizadas diretamente pelo SIGACFG.  Entretanto algumas tabelas não possuem a possibilidade de alterar o compartilhamento e estão travadas em modo exclusivo.  **Tabelas Contrato Modelo Nova Comercialização com compartilhamento liberado:**  NJR - Contratos NN7 - Previsão financeira NNY - Cadencias NNF - Despesas Corretores NN8 - Fixação Contrato NKA - Composição de Preços N84 - Condição de pagamento NC9 - Despesas Regra Fiscal N9A - Regras Fiscais  N9J - Relacionamento regras fiscais ND1 - Fixação X Previsão    **IMPORTANTE:**  1) Toda alteração deve primeiro ser realizado em base de homologação, sendo realizado todos os testes das rotinas criticas pelos usuários chave com os dados atuais da base de produção.  2) Antes de qualquer alteração, deve ser realizado backup do banco e ambiente.  3)A alteração do compartilhamento afeta diretamente o controle de numeração automático do Protheus. É aconselhado realizar essa manutenção com um especialista para que não haja erro de duplicidade de registros.  **MAIS INFORMAÇÕES:**   * [Nova Comercialização](https://tdn.totvs.com/x/BigXFg) * [Alterar compartilhamento de tabelas via SIGACFG](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026077191-MP-SIGACTB-Como-alterar-o-compartilhamento-de-tabelas-ap%C3%B3s-bloqueio-realizado-a-partir-da-LIB-vers%C3%A3o-20181015) |
| **Observações:** | Aqui foram registradas as considerações importantes na análise de base, em relação ao compartilhamento de tabelas do contrato, para que efetue a validação.  Caso realize as validações e ainda ocorra o problema, será necessário solicitar auxilio via Suporte TOTVS.  Há a Consultoria In loco (solicitar diretamente à seu Gerente de atendimento TOTVS). |
