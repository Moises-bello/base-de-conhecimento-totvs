---
content_hash: 9fd9efa18856aa9e591a0e8d7a444286695c96a421397b4b2f515b7b750d0c43
fetched_at: '2026-06-29T00:09:50.686475+00:00'
page_id: '435106767'
product: rm
source: tdn-rm
title: RMFIS00017_Melhoria na geração dos Valores de ajustes (C177 / C197 / D197 /
  E115)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435106767
version: 4
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Fiscal |
| **Versões:** | 12.1.22 (mediante script específico) e superiores |
| **Ocorrência:** | Temos tido muitas demandas de vários clientes solicitando alterações contínuas na forma como geramos os Registros C197, D197 e E115 no Sped Fiscal que se referem a “**Outras Obrigações Tributárias, Ajustes e Informações provenientes de Documento Fiscal**”, “**Outras obrigações tributárias, ajustes e informações de valores provenientes do documento fiscal**” e “**Informações Adicionais da Apuração – Valores Declaratórios**”, respectivamente.  Essa alta demanda se deve ao fato de que fica a cargo de cada um dos Estados Brasileiros regular sua forma de exigir a apresentação desses registros.  A ideia com esta especificação é flexibilizar a geração desses registros para os clientes da Linha RM e substituir as regras atuais de campos complementares no lançamento e no item e, também, reduzir/eliminar a inclusão manual do E115. |
| **Ambiente:** |  |
| **Passo a passo:** | **1. Cadastro de Ajustes**  Foi criado o Cadastro "**Código de Ajuste**" onde o usuário poderá parametrizar os ajustes defaults que afetam suas operações por Estado. Para acessar: Gestão Fiscal | Cadastros Específicos | Mais...  As fórmulas a serem utilizadas neste cadastro devem ser criadas no Gestão Fiscal.        Para mais detalhes sobre o cadastro acesse:    **2. Processo de vínculo entre CFOP e Ajuste**  Foi criado o "**Processo de associação de Códigos de Ajuste do SPED**" no Cadastro de CFOP onde o usuário deverá associar os Cadastros de Ajustes criados no item à Natureza de Operação. Podem ser associados vários CFOPs para vários códigos de ajuste ao mesmo tempo.    Para mais informações sobre o processo acesse: [FISCAL01-6575 DT Processo de Associação Ajuste SPED x Natureza de Operação](http://tdn.totvs.com/pages/viewpage.action?pageId=433241007)    **3. Lançamento Fiscal e Item do Lançamento Fiscal**  Foi criado no Lançamento Fiscal (Situação Tributária) e no Item do Lançamento Fiscal um anexo para armazenar os valores de ajustes e os valores adicionais. Esses valores são calculados automaticamente no momento da inclusão do lançamento fiscal (e também no processo de Escrituração) com base nos defaults informados no CFOP. Serão selecionados apenas os ajustes para o Estado da Filial do Lançamento Fiscal.  Havendo necessidade, existe a opção de inclusão, edição e exclusão manual diretamente no lançamento/item.    Para mais detalhes sobre este item acesse: [FISCAL01-6998 DT Inclusão de lançamento - Carregar Defaults de Ajuste](http://tdn.totvs.com/pages/viewpage.action?pageId=435106700)    **4. Sped Fiscal**  Os Registros C177 (versão 3.0), C197, D197 e E115 passam a ser gerados com base nos novos Anexos.  O Registro C177 permanece com a forma de geração atual até a competência de dezembro de 2018 e a partir de janeiro de 2019, passa a ser gerado com os valores do novo anexo do Item.  No caso do Registro E115, o sistema mantém as duas origens de dados: os novos anexos criados no Item e no Lançamento e, também, os valores informados manualmente no Período de Apuração.    Para mais informações acesse: |
|  |  |
| **Observações:** | 1. Para ter acesso a esta implementação no Release 12.1.22 solicite o script de criação das tabelas ao nosso Suporte e atualize sua Biblioteca para o último Patch . 2. Após a execução do script, será necessário dar permissão de acesso ao Perfil do usuário e reiniciar o serviço do Host. DICA: Caso o sistema não apresente os cadastros/processo, recrie o arquivo \_Broker.dat |
