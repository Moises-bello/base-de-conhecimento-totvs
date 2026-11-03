---
content_hash: f112126bec07d79467e0d8905907fad02b1c988730a45d994099e8d6055ad8d6
fetched_at: '2026-06-29T00:11:12.671929+00:00'
page_id: '656060905'
product: rm
source: tdn-rm
title: Sincronizando o Portal de Imóveis com o TCGI
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=656060905
version: 8
---

Conforme demonstrado na arquitetura o Portal de Imóveis usa a estrutura de WebServices da TOTVS para troca de informações e para que este processo funcione é necessário parametrizar alguns dados no TOTVS RM e no Portal de Imóveis.

#FF9000Parametrização no TOTVS RM

Para realizar o sincronismo dos dados entre Portal de Imóveis e RM devemos habilitar os WebServices conforme documentação do link a seguir:

Ainda no RM devemos agora habilitar as actions usadas no processo de comunicação de dados, para isto vamos seguir os passos abaixo:

1. Iniciamos o processo com a atualização das actions do sistema. Para isto devemos acessar o menu de "Serviços Globais" e depois selecionar "Actions do Sistema";
2. Ao abrir a tela de actions, selecione o menu de "Processos" e selecione "Atualização de Actions Cadastradas";
3. Ainda no menu de "Serviços Globais", acesse a opção de "Servidores de Aplicação" e no menu "Processos" selecione "Carregar dados de descrição dos serviços". *Este procedimento pode demorar até 5 minutos, favor acompanhar a janela de mensagens no rodapé do TOTVS;*
4. Feito este processo podemos chamar a URL do portal de vendas – Portal de Imóveis acessar a opção backend > Sincronizar. Ao clicar nesta opção, caso haja alguma action para ser parametrizada o sistema informará o nome destas. Estes serão os nomes usados nas etapas seguintes do processo de parametrização das actions;
5. Se ao tentar sincronizar o Portal de Imóveis com o RM apareceu a tela acima com os nomes das actions que necessitam parametrização, então acesse novamente o RM em Serviços Globais > Servidores de Aplicação. Clique no botão para adicionar um novo registro e ao abrir a tela de inclusão, clique no botão para listar os ID´s dos servers cadastrados. Ao abrir a janela de pesquisa, digite no campo descrição o nome de uma das actions listadas na tela do Portal de Imóveis (vide nomes no quadro vermelho). Selecione o registro que aparecer com esta descrição e tecle OK;
6. Na tela de cadastro, coloque o valor "-1" no campo "Número máximo de registros" e clique em Salvar;
7. Repita este processo a partir da etapa 5 enquanto houverem nomes na janela vermelha da tela de sincronismo do Portal de Imóveis.
#FF9000Sincronia de Empreendimentos

A partir da versão **12.1.2205**, o sincronismo de empreendimentos no Portal de Imóveis ocorrerá apenas dos empreendimentos ativos no sistema.

Ao sincronizar pela primeira vez os empreendimentos irão nascer no Portal de Imóveis como inativos, e o usuário deverá ativá-los no menu [Empreendimentos (Clique Aqui!)](https://tdn.totvs.com/display/LRM/Editando+Empreendimentos)

Após esta ativação o RM irá registrar em qual domínio o mesmo foi ativado e irá liberar este empreendimento para uso somente neste domínio onde foi ativado.

Caso o empreendimento já esteja ativo em outro domínio do portal de imóveis o sincronismo não poderá ser realizado enquanto o empreendimento não for desativado no domínio anterior.

Exemplo:

O portal de imóveis possui dois domínios, *dominio1.portaldeimoveistotvs.com.br* e *dominio2.portaldeimoveistotvs.com.br*

No *dominio1* o Empreendimento TOTVS foi ativado e feita a sua sincronia.

No *dominio2* este mesmo empreendimento não poderá ser sincronizado, visto que já está em uso no *dominio1.*
