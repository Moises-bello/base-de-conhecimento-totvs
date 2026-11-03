---
content_hash: 4ec74c0f71d4c9b64ee967cc131ac52904213dcceab8387f7d207ffed6c90c89
fetched_at: '2026-06-29T00:08:37.625710+00:00'
page_id: '284880251'
product: rm
source: tdn-rm
title: URL's Externas
type: documentation
url: https://tdn.totvs.com/display/LRM/URL%27s+Externas
version: 36
---

As URL's externas são os links que a instituição pode disponibilizar para o aluno acessar e ser direcionado ao clicar.  
Para realizar o cadastro das URL's externas, basta acessar:

**MDI | Serviços Globais | Serviços | URL Externa**

**Menu | URL's Externas:**

Tanto no Portal do Professor como no Portal do Aluno, ao clicar em um item do submenu, o usuário será redirecionado para o link cadastrado. 

IMPORTANTE

Ao MARCAR o parâmetro na MDI : 

3
incomplete
 **ENVIA CONTEXTO :**Quer dizer que no link que o aluno for direcionado, irá conter alguns os dados do contexto global RM de forma aberta como por exemplo código da coligada, filial dentre outras informações.  
 **Exemplo: https://www.totvs.com/?Context=[CodSistema=S;Environment=Delphi;CodUsuario=3030;CodUsuarioServico=-1;CodColigada=1;CodFilial=1&key=rw\01\9A\0C\F4\7F\ED\05\DA\D5N\00\85\FD\C2\0C\0E\EEK\B0\EF\2A\88\D4\C4\0A\8Bt\D9\16\;**  
  

Ao DESMARCAR o parâmetro na MDI : 

4
incomplete
 **ENVIA CONTEXTO :**Quer dizer que no link que o aluno for direcionado, NÃO irá conter o contexto global RM.  
  
**Exemplo: https://www.totvs.com/?key=rw\01\9A\0C\F4\7F\ED\05\DA\D5N\00\85\FD\C2\0C\0E\EEK\B0\EF\2A\88\D4\C4\0A\8Bt\D9\16\**  
  

**Para efeito de customizações do Portal do Aluno do TOTVS Educacional com páginas externas, em ambos os casos acima, será enviado na URL um parâmetro criptografado (com o nome padrão "key" e parametrizado e explicado conforme abaixo) com os dados de contexto do aluno que está logado no Portal do Aluno, como por exemplo RA, coligada, filial dentre outras informações. Maiores informações de customização com páginas externas no link abaixo:**

**Observação: A URL cadastrada no campo "URL Externa" não deve possuir nenhum conteúdo com ENCODE aplicado. Ou seja, qualquer conteúdo ou parâmetro informado nesta URL deve ser com o seu conteúdo nativo. Isso é necessário, porque durante o carregamento desta URL pelo Portal Educacional será aplicado um ENCODE com todo o conteúdo da URL, adicionando as informações mencionados logo acima. E desta forma, se já tiver sido informado uma URL com ENCONDE neste cadastro de URL Externa, o conteúdo será alterado devido a duplicidade da aplicação do ENCODE.**

Alteração do nome do parâmetro "Key"

O nome do parâmetro onde contém os dados do Contexto do aluno, adicionados nas URL's externas cadastradas, pode ser alterado através do parâmetro chamado "**ExternalUrlKeyName**" no arquivo Web.Config da pasta FrameHTML. O valor padrão para este parâmetro é "**key**", e pode ser alterado caso a URL de destino já espere um parâmetro com este mesmo nome, evitando assim conflitos ao abrir aplicações externas ou de terceiros.
