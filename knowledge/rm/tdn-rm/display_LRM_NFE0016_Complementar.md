---
content_hash: c83cd7c8a907e154852ea8ff54b85eaa1981332efe4d41c7f5ac613eecd72cfc
fetched_at: '2026-06-29T00:08:09.923298+00:00'
page_id: '240295445'
product: rm
source: tdn-rm
title: NFE0016_Complementar
type: documentation
url: https://tdn.totvs.com/display/LRM/NFE0016_Complementar
version: 16
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | NF-e - Nota Fiscal Eletrônica |
| **Versões:** | A partir da versão 11.52 |
| **Ocorrência:** | NF-e Complementar |
| **Passo a passo:** | **Introdução**   Este Documento auxilia a criação de um movimento básico para complementar impostos de uma NF-e no sistema. Qualquer NF-e complementar deve ser emitida de acordo com a legislação vigente mesmo que esteja em desacordo com este documento.  **Criando uma NF-e Complementar**  1. Parametrize um movimento de NF-e normalmente;  2. Acesse o RM Nucleus no seguinte menu: Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Outras Movimentações/Vendas/Compras (dependendo da classificação do tipo movimento desejado) | Selecione o Tipo de movimento e clique em Parametrizar.  **Etapa Mov – Outros Dados:** Nesta etapa marque a opção “Usar Copia de Movimento por referência”, selecionando o motivo  “6 – Complementar/Retificadora”;    **Etapa Fis – NF-e:** Nesta etapa marque a opção de Enviar NF-e (Conforme regra da empresa);    **Etapa Item – Preços:** Nesta etapa marque a opção “Aceitar Preço Zero”;    **Etapa Item – Identificação:** Nesta etapa marque a opção “Permite Item com Quantidade Zero” (Caso também for criar complemento de valor, sem quantidade);    3. **Produto:**Acesse os Menu Cadastros | Produtos e Serviços e Cadastre um Produto Genérico para complementar o Imposto.    4.**CFOP (Natureza de Operação):** Acesse o cadastro da natureza de operação (CFOP) | edite a natureza a ser utilizada | aba Tributação ICMS/IPI | edite a regra de ICMS | na aba identificação o tipo de tributação tem que ser “Outros” | na aba Outros dados marque o flag Operação complementar com o tipo de ICMS a ser complementado | salve as configurações.  **IMPORTANTE: A situação tributaria do ICMS deve ser a mesma utilizada na NF-e a ser complementada.**    5. Acesse o menu do tipo de movimento criado para a NF-e complementar (Compras/Vendas/Outras movimentações) | preencha o filtro com o tipo de movimento e filial | gere um movimento por referencia através do menu Processos | "assistente de copia por referencia“.    Preencha o filtro para referenciar ao movimento original (NF-e que será complementada):    **Importante:** Os itens não serão copiados você deverá utilizar o item cadastrado anteriormente na etapa 5.  6. Preencha apenas a quantidade e os valores que serão complementados (conforme a necessidade).    **Observação:** Pode ser preenchido a quantidade, o valor ou ambos, conforme a necessidade da empresa.  Após a realização do passo a passo proceda com o envio da NF-e Normalmente. |
| **Observações:** | Para mais informações:  [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
