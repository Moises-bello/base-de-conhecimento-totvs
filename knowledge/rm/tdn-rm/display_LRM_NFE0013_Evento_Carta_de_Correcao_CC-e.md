---
content_hash: 0499f791107bc17aae5121408ec63728ad0672cc01347b7fffbc1e06750d508d
fetched_at: '2026-06-29T00:08:12.128127+00:00'
page_id: '243635327'
product: rm
source: tdn-rm
title: NFE0013_Evento_Carta_de_Correcao_CC-e
type: documentation
url: https://tdn.totvs.com/display/LRM/NFE0013_Evento_Carta_de_Correcao_CC-e
version: 1
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | NF-e - Nota Fiscal Eletrônica |
| **Versões:** | A partir da 11.52 |
| **Ocorrência:** | Evento - Carta de correção |
| **Passo a passo:** | **Introdução:**  O processo de Carta de Correção Eletrônica é utilizado para realizar correções na Nota Fiscal Eletrônica, onde não serão aceitas as correções referentes às variáveis consideradas no cálculo do valor do imposto, tais como: valor da operação ou da prestação, base de cálculo e alíquota; a dados cadastrais que impliquem alteração na identidade ou no endereço de localização do remetente ou do destinatário; à data de emissão da NF-e ou à data de saída da mercadoria, para maiores informações consulte a SEFAZ.  Será necessário dar permissão aos usuários que emitirão a CC-e através do seguinte menu: Cadastros | Segurança | Perfis | Edite o perfil dos usuários | Acesso a menus | é necessário dar permissão no menu “Envio de Evento NF-e” e “Consulta Evento NF-e” conforme imagem abaixo:    **2. Parametrizações**  Acesse o RM Nucleus no seguinte menu: Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento  | Integrações | Fiscal| Parâmetros por filial | selecione a filial e clique em parametrizar | Etapa 5 – Ambiente CC-E | e parametrizando da seguinte maneira:      **OBSERVAÇÃO: A Carta de Correção Eletrônica deve ser enviada para o mesmo ambiente de autorização, Produção ou Homologação.**Deve se atentar tambem se a Filial esta ou não em horario de verão e em qual fuso horario se encontra.  **3. Gerando a Carta de Correção Eletrônica**  Acesse o RM Nucleus no seguinte menu: Vendas | Faturamento | SPED NFE (Estadual) preencha o filtro desejado, selecione a NF-e a ser corrigida, e clique em | Processos | Envio de evento NF-e .    Será aberta uma nova visão com o nome “Envio de evento NF-e”, selecione o Tipo de Evento como Carta de Correção Eletrônica, preencha a solicitação de correção e clique em Executar.      **OBSERVAÇÃO:** **O texto digitado para a correção não pode ter quebras de linha(<<Enter>>).**  Após realizar o envio da CC-e, é necessário realizar a consulta da Carta de Correção e salvar o XML autorizado da Carta. Para realizar a consulta acesse o menu | ANEXOS | EVENTOS DA NF-E:    Selecione o evento e clique em | PROCESSOS | CONSULTA EVENTO NF-E:    **Informações Adicionais:**  A Carta de Correção Eletrônica não é impressa.  De acordo com a [Nota Técnica 2011.003](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=tsiloeZ6vBw=) é de existência **APENAS DIGITAL,**sendo necessário apenas enviar o arquivo XML da Carta de Correção Eletrônica para o cliente.  Uma vez a CCe sendo **enviada com sucesso** para a SEFAZ, ela se torna um **evento** da NFe (que ficará "atrelada" a mesma) e poderá ser **CONSULTADA**através do [**Portal Nacional da NFe**](http://www.nfe.fazenda.gov.br/portal/principal.aspx) como um evento da NFe. |
| **Observações:** | Para mais informações:  [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
