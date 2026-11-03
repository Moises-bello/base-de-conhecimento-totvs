---
article_id: 360015771071
category: eSocial - Parametrizador
content_hash: f119ad9785bd548a5c03ec17044184c860d66553e4c0f7675fd61a68c01edb89
fetched_at: '2026-06-28T22:47:06.342873+00:00'
product: rm
section_id: 1500000834501
source: central-rm
title: RH - RM - FOP - eSocial -  Associação de Filiais RM e TAF
type: support-article
updated_at: '2026-04-17T19:30:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015771071-RH-RM-FOP-eSocial-Associa%C3%A7%C3%A3o-de-Filiais-RM-e-TAF
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24484884967959)**Tempo aproximado para leitura:**00:02:00 min**  
  
**Dúvida**  
Como associar as filiais entre RM e TAF?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as Versões

**Solução**  
Existem as parametrizações para o caso da empresa que só possui uma coligada e várias filiais na mesma coligada, a empresa que possui N coligadas mas irá unifica-las dentro do TAF para facilitar seu envio ao eSocial ou a empresa que possui N coligadas, mas por questões de segurança precisa liberar acesso por coligadas dentro do TAF.  
[CLIQUE AQUI](http://tdn.totvs.com/display/public/TAF/Complemento+de+Empresa+-+TAFA050+-+TAF+-+P12#ComplementodeEmpresa-TAFA050-TAF-P12-OutrosExemplosdeConfigura%C3%A7%C3%A3o(ERPxTAF)) para ver o link para ajudá-lo a entender a integração com o TAF.   
Veja também vídeos exemplificando o cadastro de [grupo de empresa](https://www.youtube.com/watch?v=5r-1dJSC8xQ&index=14&list=PLXa8l0dq5zRmfNY744BnO4Db_SH917WbI), [empresa](https://www.youtube.com/watch?v=TC44nnW6Zzs&index=9&list=PLXa8l0dq5zRmfNY744BnO4Db_SH917WbI) e [filiais](https://www.youtube.com/watch?v=XTcodtMYHxE&index=11&list=PLXa8l0dq5zRmfNY744BnO4Db_SH917WbI).  
Veja o roteiro com mais detalhes que complementam os vídeos: [Cadastros Taf](http://tdn.totvs.com/display/public/TAF/Cadastro+da+Empresa+-+TAF+-+P12) Configurar o complemento cadastral e com atenção para configuração da matriz, pela qual será utilizada para envio ao site do eSocial: [CLIQUE AQUI](https://www.youtube.com/watch?v=RZcqwCJ8PeQ&index=15&list=PLXa8l0dq5zRmfNY744BnO4Db_SH917WbI).  
Uma vez cadastrados os complementos no Taf, segundo sua necessidade, agora vamos configurar o RM acessando o menu **Configurações | Parametrizador | eSocial | Integração com o TAF**.  
  
Nesta tela iremos informar a configuração da matriz que é responsável para enviar as informações ao Ret/eSocial:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360010830271)  
  
No campo em destaque poderá ficar 0101 representando grupo 01 e filial 01, aquela configurada como matriz de acordo com orientação do último vídeo.  
  
**Utilizando mais de uma filial e destinando os eventos para filial correspondente**  
  
Ao marcar o parâmetro “Utilizar relacionamento Filial RM x Filial TAF para eventos de funcionário” iremos avaliar alguns pontos:

* Na próxima página do parametrizador, será necessário associar as filiais do RM com as filiais cadastradas no Taf;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360010830291)

Poderá marcar a opção “Utilizar a filial padrão”, caso não marque será gerado mensagem que não pode localizar a filial (TAFFIL).

       *Exemplo:*

Caso algum evento do funcionário tenha sido enviado ao Taf para alguma filial e a mesma não esteja configurada na lista citada acima, o RM irá associar tal evento para a filial sugerida, como no exemplo abaixo, a filial 03:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360010803632)

Erros mais comuns:

* **Código erro TAF: 803 Certifique-se de que seu ambiente TAF, TSS e RM estão atualizados**

Solução 1:  
Acesse o TAF e em seguida o cadastro de complemento de empresas em: **Atualização > Empresa > Complemento Cadastral.**  
  
Copiar o código contido no campo "Cod Filial"  
  
Acesse o Parametrizador do RM Labore aba integração com TAF em: **Configurações > Parametrizador > eSocial > Integração com TAF** e informe o valor do campo Cód. Filial do complemento cadastral.  
  
[Telas aqui](http://tdn.totvs.com/pages/releaseview.action?pageId=359473627#ErroseA%C3%A7%C3%B5es-2165554)

Solução 2: A configuração do serviço de integração não foi realizada para as empresas do TAF que os dados estão sendo enviados. Neste caso será necessário ajustar a configuração da seção [TAF\_CFGJOB] conforme abaixo:  
  
[TAF\_CFGJOB]  
Main=TAF\_CFGJOB  
Instances=1,1  
\*PrepareIn=ALL  
nRefreshRate=50  
ENVIRONMENT=P12  
  
\* Utilizando a palavra ALL, neste caso o server vai considerar todos os grupos contidos no arquivo de empresas do Protheus/TAF; Ex PrepareIn=ALL (RECOMENDADO)  
  
Obs: Editar via interface SRVWIZARD. Acesse [aqui](http://tdn.totvs.com/pages/releaseview.action?pageId=329024902).

* **O valor 'XXXXXX' informado na tag XXXXXXXX não existe na base de dados.**

Vamos avaliar a situação, estou enviando eventos dos funcionários da matriz com sucesso, já fiz o envio de todos os eventos predecessores do funcionário e agora ao tentar enviar um funcionário da filial Z, não está processando corretamente e gera a mensagem citada acima. O que fazer?  
  
Provavelmente foi configurado no Taf uma estrutura de grupo de empresa, empresa e matriz que inicialmente restringe a visualização de tais registros entre grupos, para melhor configurar seu sistema basta seguir este [roteiro](http://tdn.totvs.com/pages/releaseview.action?pageId=342312661).  
  
  
**Importante**  
Nosso suporte Taf pode apoia-lo em dúvidas pontuais sobre o roteiro sugerido, antes de executa-lo, sugere-se fazer um backup dos bancos de dados TAF, TSS e RM bem como de seus diretórios de instalação (TAF/TSS).
