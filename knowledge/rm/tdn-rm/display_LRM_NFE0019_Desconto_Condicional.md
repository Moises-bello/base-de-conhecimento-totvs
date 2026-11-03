---
content_hash: d8efa143f2ef4e9ddcbd925bb04d00daa7c440a9f3924c666411cd891376d4f4
fetched_at: '2026-06-29T00:08:09.917432+00:00'
page_id: '240295444'
product: rm
source: tdn-rm
title: NFE0019_Desconto_Condicional
type: documentation
url: https://tdn.totvs.com/display/LRM/NFE0019_Desconto_Condicional
version: 4
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | NF-e - Nota Fiscal Eletrônica |
| **Versões:** | A partir da versão 11.52 |
| **Ocorrência:** | Desconto condicional |
| **Passo a passo:** | **Introdução:**   As instruções deste documento é uma sugestão para preenchimento do campo Desconto Condicional, uma vez que o mesmo só é preenchido através de fórmulas. As regras específicas de cada cliente para concessão do desconto condicional devem ser observadas.  Estas instruções não se aplicam na integração com o Educacional, uma vez que os campos de descontos, tanto o condicional como o incondicional, são preenchidos através da Classificação de Bolsas.  **Objetivo:**  Auxiliar na parametrização correta para que o “Desconto Condicional ” tanto no movimento quanto no item sejam levados para o XML da NF-e.  **Criando a formula:**  Para criar a formula realize o seguinte procedimento: No RMNucleus vá em: Cadastros |Formulas | crie as seguintes formulas:  **Desconto Condicional para o Movimento**  Cod: DMC  TABMOV ('VALOREXTRA1' , 'V')  **Desconto Condicional para o Item**  Cod: DIC  TABITM ('RATEIOEXTRA1' , 'V')    **Editando o tipo de movimento:**  Após criar as formulas será necessário parametrizar o tipo de movimento para a utilização do desconto condicional. Para isso acesse o RM Nucleus no seguinte menu: Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Outras Movimentações/Vendas/Compras (dependendo da classificação do tipo movimento desejado) | Selecione o Tipo de movimento e clique em Parametrizar.  **Etapa Mov – Valores Financeiros 1/4:** Habilite o campo valor extra 1.    **Etapa Mov – Valores Financeiros 2/4:** Informe as fórmula para calcular o desconto condicional no Movimento e no Item informando as fórmulas criadas anteriormente.    **Habilitando rateio proporcional:**  **Etapa Mov – Valores financeiros 2/2:** Ao utilizar desconto no movimento para que o mesmo seja levado para o XML é obrigatório que o mesmo seja rateado pelos itens podendo ser condicional (formula)o proporcional (quantidade de itens e valor).    Após a realização do passo a passo proceda com o envio da NF-e Normalmente. |
| **Observações:** | Para mais informações:  [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
