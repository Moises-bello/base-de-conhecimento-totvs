---
content_hash: 77da2d7388eb8b757b1454fe4b1100d74195ffee97b5343f2d405cb0fdf6135d
fetched_at: '2026-06-28T21:35:22.628182+00:00'
page_id: '238034806'
product: fluig
source: tdn-fluig
title: Conversão de legado Fluig ESB
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=238034806
version: 7
---

Fique atento!

O TOTVS ESB não é mais ofertado por se tratar de uma solução legada. A nova solução para realizar integrações é o TOTVS iPaaS. Saiba mais detalhes **[aqui](https://www.totvs.com/totvs-ipaas/)**. 

# Índice

4true.\*ndicenone

# Objetivo

---

A partir da versão 12 do Fluig ESB há a necessidade de converter os diagramas e arquivos de configuração para um novo formato, devido ao novo conceito de implantação e configuração nos servidores.

O objetivo desse manual é demonstrar como converter os diagramas da versão 5 para dentro do TDS (TOTVS Developer Studio) utilizando o plugin Fluig ESB. É necessário que o usuário tenha instalado o TDS juntamente com o plugin Fluig ESB.

# Importação de diagramas

---

Para importar os diagramas oriundos da versão 5 do ESB para dentro do TDS, deve-se acionar o menu **Window → Open Perspective → Other...**, selecionar a perspectiva TOTVS ESB e clicar em OK.

A área de trabalho será atualizada e no painel esquerdo será exibido o **ESB Navigator** que conterá os projetos com os diagramas do ESB.

samples1Passo 1

Clicando com o botão direito no centro do **ESB Navigator** selecione o item de menu **New → ESB Project**. Ao exibir a tela, preencha com todas as informações e após clicar no botão **Finish** para criar um projeto.

2Passo 2

No painel **ESB Navigator** aparecerá o projeto criado com uma estrutura de pastas padrão. Dentro desse projeto serão criados os diagramas para o Fluig ESB. Para importar os diagramas da versão 5, clique com o botão direito em cima do projeto e selecione o item **Import → Import File**.

Abrirá a tela semelhante ao abaixo solicitando que o usuário identifique o arquivo dos diagramas em que se deseje importar. Através do botão **Browse**... seleciona-se o arquivo esb-config.xml da versão 5 do Fluig ESB para importar. Clique em **Finish** para finalizar o procedimento e iniciar os procedimentos de importação.

3Passo 3

O resultado é exibido no painel **ESB Navigator**. Cada diagrama contido no arquivo esb-config.xml se tornou um arquivo diferente com a extensão .esb dentro do projeto selecionado previamente. Os arquivos correlatos também foram importados (.xsl, .tcl, etc.) para o projeto facilitando o manuseio desses arquivos.

A seguir tem-se um comparativo do diagrama da versão 5 do Fluig ESB com a versão atual dentro do TDS.

4Passo 4

Cabe salientar que o Fluig ESB 12 não utiliza mais nenhum arquivo da versão 5, somente os arquivos que foram importados para o TDS. Ainda, os arquivos com a extensão STD (.std) referenciados pelos componentes Identifier, não são mais necessários, pois as informações foram extraídas e impostas nas propriedades do componente.

Para que os diagramas sejam ativados no servidor ESB, os mesmos deverão ser publicados. Certifique-se de que o servidor Fluig ESB se encontra em execução. Com o servidor “no ar”, o usuário deverá abrir um dos diagramas (arquivo .esb) dentro do TDS e clicar no meio do diagrama com o botão direito e acessar o menu **Deploy to ESB Server...** conforme figura ao lado.

5Passo 5

Com isso será exibida uma tela permitindo ao usuário selecionar o servidor Fluig ESB cadastrado anteriormente. Ainda permite que o usuário opte por somente adicionar o diagrama atual aos diagramas existentes no ESB ou se deseja substituir todos os diagramas existentes pelo selecionado. Ao clicar no botão **Finish**, o processo de *deploy* será iniciado.

O mesmo procedimento deverá ser realizado para os outros diagramas até que todos arquivos .esb estejam devidamente publicados no Fluig ESB. Para habilitar a execução dos diagramas deverá reiniciar o servidor ESB. Não é necessário enviar manualmente os arquivos correlatos (.xsl, .tcl, etc.) pois o processo de *deploy* se encarrega de enviar esses arquivos.
