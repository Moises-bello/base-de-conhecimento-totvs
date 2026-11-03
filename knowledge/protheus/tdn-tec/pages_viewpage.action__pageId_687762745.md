---
content_hash: 11adee874e5913129725d2e1a86edd59788e39a1e9b9dae0cb2d3d757c92e990
fetched_at: '2026-07-02T19:24:27.904454+00:00'
page_id: '687762745'
product: protheus
source: tdn-tec
title: Extensão VSCode
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=687762745
version: 5
---

A extensão para VSCode do **PROBAT** permite que possamos analisar visualmente linha a linha a cobertura de código obtida através da execução dos testes.

Para que funcione corretamente, é preciso que o **PROBAT** tenha gerado um arquivo JSON com os dados dos fontes e suas respectivas coberturas, além disso é preciso configurar no VsCode a localização e nome do arquivo.

### Download

> A extensão ainda não foi lançada oficialmente na loja da VSCode, porém é possível obtê-la baixando o arquivo de instalação (VSIX) através do link abaixo.

| Versão | Arquivo |
| --- | --- |
| v0.0.2 |  |

### Instalando

Após obter o arquivo .vsix do **PROBAT**, recomendamos seguir a documentação oficial do VsCode com os passos para a instalação da extensão.

Acesse a página: <https://code.visualstudio.com/docs/editor/extension-marketplace#_install-from-a-vsix>

Ou instale diretamente do VSCode. Com ele aberto, acesse no menu lateral a área de extensões , após isso clique em na parte superior para abrir o menu, e então acesse "Install from VSIX...", conforme imagem abaixo:

Agora é só informar onde está o arquivo [probat-x.x.x.VSIX] para que o VSCode iniciar a instalação.

### Configurando

Como dito anteriormente, temos que informar ao VsCode onde encontrar o arquivo JSON gerado pelo **PROBAT** com as informações de Cobertura.

1 - Tecle [Ctrl + ,] para acessar a tela de configuração do VsCode;   
2 - Selecione as configurações da [Workspace];   
3 - Vá em [Extensions];   
4 - Procure a seção [PROBAT];   
5 - Informe em [Coverage: File] o arquivo gerado pelo **PROBAT**.

Conforme figura abaixo:

### Visualizando a Cobertura

Após a configuração, agora é possível visualizar a cobertura sobre seus código, desde que a informação tenha sido gerada no arquivo JSON.

Pra isso, siga os passos:

1 - Abra o arquivo que deseja visualizar a Cobertura;   
2 - Após abrir, digite: [Ctrl + Shift + P ] para abrir a caixa de comandos;   
3 - Digite: [PROBAT - Show Code Coverage];

##### OK

Caso tudo esteja OK, a extensão irá decorar seu fonte com cores distintas e teremos algo como:

Sendo:

* Linhas Cobertas: Cor Verde
* Linhas NÃO Cobertas: Cor Vermelha
* Linhas não debugáveis: sem decoração, nada muda.

##### Erro

Caso o fonte não tenha sido decorado com a cobertura veja nos logs do VsCode, aba OUTPUT opção probat, algo como:

```
[probat] [coverage] start show ....  
[probat] [coverage]   [ERROR] arquivo inexistente ou inválido!  
[probat] [coverage] end show ....
```

Nesse exemplo, o arquivo informado na configuração não foi encontrado ou possui formato incorreto.

### Informações importantes

##### Uso somente local

Na versão atual 0.0.2, ainda somente é possível utilizar esse recurso localmente, ou seja, o VsCode e o Appserver onde é executado devem estar na mesma máquina para que o arquivo gerado esteja ao "alcance" do VsCode.

Está previso para as próximas versões que essa comunicação permita uma arquitetura mais flexível.

##### BUG

Por vezes, após uso contínuo da visualização em tela da cobertura de código de um ou mais fonte, pode ocasionar um comportamento inadequado de ao acionar a rotina "Show Coverage" a cobertura em tela ocorrer em linhas erradas.

Para resolver esse comportamento, basta reiniciar o VsCode e ligar novamente o "Show Coverage".

Já existe um chamado [DTTLPP-2097] para correção desse comportamento.
