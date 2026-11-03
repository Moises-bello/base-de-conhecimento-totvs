---
content_hash: 8f356c5a5ddc59ef682cf06f9672539c5d86e371212bcb36b8fa073680110948
fetched_at: '2026-06-29T00:08:53.192961+00:00'
page_id: '344462280'
product: rm
source: tdn-rm
title: Campos não-obrigatórios apresentados no Log ao gerar XML
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=344462280
version: 2
---

|  |  |
| --- | --- |
| **Produto:** | TOTVS Folha de Pagamento |
| **Dúvida:** | Campos não-obrigatórios apresentados no Log ao gerar XML |
| **Resposta:** | Alguns campos não obrigatórios poderão ser apresentados no Log de Erros e Avisos ao gerar determinado XML. Deve-se estar atento se tais campos estão sendo apresentados como "Avisos" ou "Erros".  Para os itens apresentados como "Avisos", o sistema não irá impedir a integração e transmissão do evento. Já para aqueles apresentados como "Erros", deve-se corrigir a informação antes de continuar com demais processos.  Fique atento aos parâmetros abaixo localizados em "Configurações > Parametrizador > eSocial > Configurações Gerais 1":    ***• Não gerar aviso para registro não obrigatório quando desconsiderado no XML***  Esse parâmetro fará com que o sistema desconsidere os grupos/registros não obrigatórios, ou seja, essas informações serão ocultadas do log.  ***Exemplo:*** Dentro do cadastro de funcionário os campos referente ao documento CNH não estão preenchidos, sendo assim, ao gerar o XML do evento/validador da base de dados, com o parâmetro desmarcado, será apresentado no log de aviso uma mensagem como: "Registro 'CNH' não foi gerado porque os campos obrigatórios ('categoriaCnh', 'dtValid', 'nrRegCnh', 'ufCnh') não estão preenchidos."  Caso esse parâmetro seja marcado, avisos como o citado acima serão desconsiderados no log.  ***• Gerar erro de preenchimento para registro não obrigatório quando tiver algum campo preenchido***  Quando este parâmetro estiver marcado o sistema irá gerar erro para registros não obrigatórios quando tiver algum campo preenchido.  Quando desmarcado, para os registros não obrigatórios que não estiverem com todos os campos obrigatórios preenchidos o sistema gera aviso informado que o registro não foi considerado no XML.    Mais informações em <http://wikihelp.totvs.com.br/WikiHelp/FOP/Fop.ConfiguracoesGerais1.aspx> |
