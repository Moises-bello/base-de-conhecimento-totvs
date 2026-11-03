---
content_hash: 67d499b3ec301b42be202b149f3ae2da0fb3e836e0e19e898c50e208b348d0b7
fetched_at: '2026-06-29T00:08:31.848981+00:00'
page_id: '273313358'
product: rm
source: tdn-rm
title: MOV0005_Exibicao_do_campo_Chave_de_Acesso
type: documentation
url: https://tdn.totvs.com/display/LRM/MOV0005_Exibicao_do_campo_Chave_de_Acesso
version: 2
---

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão de Estoque, Compras e Faturamento |
| **Versões:** | A partir da 11.52 |
| **Ocorrência:** | Exibição do campo Chave de Acesso |
| **Passo a passo:** | **Introdução:**  Este documento tem o objetivo auxiliar na parametrização do tipo de movimento para exibição da chave de acesso no movimento.  **Passo 1:**  Acessar | Ambiente | Parâmetros | Gestão de estoque, compras e faturamento | Localizar o tipo de movimento que irá aplicar a parametrização.  **Etapa Mov - Emitente/Destinatário**    Emitente deverá ser = Fornecedor  Destinatário deverá ser = Empresa  **Etapa Fis - Escrituração 1/2**  Nesta Etapa deverá ser marcada a opção “Gerar Escrituração” e no campo “Tipo Documento Escrituração” deverá ser selecionado o tipo de documento de NF-e, CT-e ou NFC-e, maiores informações sobre o cadastro do tipo de documento.    Obs: O código do modelo documento que o sistema verifica é esse:      **Etapa Fis - NF-e**  Obs: Ao acessar essa etapa e não aparecer o campo indicado, conforme imagem abaixo:    Será necessário voltar para **Etapa Mov - Emitente/Destinatário**e alterar **provisoriamente** os campos "Emitente" e "Destinatário".    Após habilitar o campo na **Etapa Fis - NF-e**  voltar a parametrização indicada anteriormente.  O campo NF-e Estadual deverá estar como "Não Integrado":    Depois de efetuar as devidas parametrizações será apresentado o campo em Integrações | Fiscal | NF-e Estadual (Caso utilizado o código do modelo do documento '55')    Caso queira habilitar a chave de acesso para CT-e ou NFC-e basta utilizar outro tipo de documento:  **CT-e**    **NFC-e** |
| **Observações:** | Para mais informações:  [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
