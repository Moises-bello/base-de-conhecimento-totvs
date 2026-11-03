---
content_hash: 39ee9867139267b1193b15f3b1d9b0130ec452937a500936f80601b8f7dde44d
fetched_at: '2026-07-02T19:24:19.688012+00:00'
page_id: '243653301'
product: protheus
source: tdn-tec
title: Aplicação de Licença (bibliotecas ctreecsv.dll e libctreecsv.so )
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243653301
version: 2
---

ctreeServer - Aplicação de Licença

A aplicação da licença liberada pela FairCom é realizada sobre a a biblioteca ctreecsv.dll ou libctreecsv.so, em ambientes com BoundServer configurado.

Abaixo, o procedimento para aplicação:

## Windows true

1. Em um diretório separado, faça uma cópia dos arquivos **ctreecsv.dll** e **fcactvat.exe**
2. Abra um Prompt de Comando (cmd) e acesse o diretório criado para este fim (para este exemplo, usaremos o path: **d:\totvs\bound**)
3. Com o Prompt de Comando aberto, execute o comando **fcactvat.exe ctreecsv.dll** e tecle <ENTER>
4. A seguir, lhe será solicitada a chave de ativação.
5. Digite a chave de ativação fornecida pela FairCom e tecle <ENTER>.
6. Em seguida, será você deverá informar os *Serial Number* que é composto por 6 dígitos. Informe-os e tecle <ENTER>
7. Por fim, se tudo ocorreu bem, a seguinte mensagem será exibida indicando o sucesso da aplicação da licença:

---

## Linux true

1. Em um diretório separado, faça uma cópia dos arquivos **libctreecsv.so** e **fcactvat**
2. Abra um Terminal e acesse o diretório criado para este fim (para este exemplo, usaremos o path: **/tmp/bound**)
3. Com o Terminal aberto, execute o comando **./fcactvat.exe libctreecsv.so** e tecle <ENTER>
4. A seguir, lhe será solicitada a chave de ativação.
5. Digite a chave de ativação fornecida pela FairCom e tecle <ENTER>.
6. Em seguida, será você deverá informar os *Serial Number* que é composto por 6 dígitos. Informe-os e tecle <ENTER>
7. Por fim, se tudo ocorreu bem, a seguinte mensagem será exibida indicando o sucesso da aplicação da licença:

---

## Observações:

* Faça um backup do arquivo ctreecsv.dll ou libctreecsv.so e reserve-o.
* Certifique-se de que o arquivo não esteja com o atributo *Read Only* (somente leitura).
* A solicitação de licenças deve ser feita a FairCom e para isto, busque orientações junto ao seu EAR - Executivo de Atendimento Relacionamento.
* Este procedimento atende a cenários com o uso do CtreeServer e CtreeServer Embarcado, conhecido como BoundServer.
* Após a aplicação da licença, lembre-se de salvar uma cópia do arquivo ctreecsv.dll ou libctreecsv.so na pasta de instalação do CtreeServer e/ou do AppServer, em caso de uso do BoundServer.

---

## Leitura recomendada
