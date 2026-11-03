---
content_hash: f86f2ccd0320a03ad3edc3ec26085c97514d0cc02314ac66d0f5fde82f7ff00c
fetched_at: '2026-06-29T00:06:26.360664+00:00'
page_id: '225261313'
product: rm
source: tdn-rm
title: TOTVS Reports Compare
type: documentation
url: https://tdn.totvs.com/display/LRM/TOTVS+Reports+Compare
version: 167
---

# Índice:

---

.\*ndice:

# Objetivo:

---

**Totvs Reports Compare**

O Objetivo do TOTVS Reports Compare é identificar divergências na geração de relatórios entre nossas atualizações.

# Introdução:

---

A partir da versão 12.1.15 a instalação do sistema colocará à disposição dos clientes o Totvs Reports Compare.

O aplicativo poderá ser encontrado no diretório defino durante a instalação (Exemplo do padrão: **C:\totvs\CorporeRM\RM.Net**) com a nomenclatura **TOTVSReportsCompare.exe**.

# Configurações:

---

Para melhor uso desta ferramenta é necessário realizar algumas configurações no ambiente.

falseConfigurações Necessárias01: TOTVSReportsCompare.exe.config.

Através do arquivo TOTVSReportsCompare.exe.config definimos várias configurações de funcionamento do Reports Compare.

xmlEclipseArquivo: TOTVSReportsCompare.exe.config










  
]]>

Tag "**LogFile**": Responsável por gerar arquivo de log de erros no caminho informado.

Tag "**MailList**": Lista de e-mails de destinatários que receberão o resultado da comparação. Para envio a mais de um e-mail use ponto e virgula (;) como separador.

Tag "**EspelhoPath**": Diretório onde os espelhos serão gerados. Recomendamos criar uma pasta exclusiva para os espelhos.

false

Para execução dos processos acionados pelas opções de “**Gerar Espelhos**” e “**Comparar**” através da opção de “**Multiprocessamento**” se deve incluir as tag’s abaixo no config TOTVSReportsCompare.exe.config.

Na tag **UserName** informe um usuário do sistema com acesso ativo e na tag **Password** a senha deste usuário.

02: TOTVSReportsRunner.exe.config

O TOTVSReportsRunner.exe, é o arquivo responsável por executar a opção de Multiprocessamento dos relatórios. Para que o mesmo execute corretamente, é necessário que os arquivos TOTVSReportsCompare.exe.config e TOTVSReportsRunner.exe.config estejam configurados da mesma forma.

xmlEclipseArquivo: TOTVSReportsRunner.exe.config








  
]]>

Tag "**LogFile**": Responsável por gerar arquivo de log de erros no caminho informado.

Tag "**MailList**": Lista de e-mails de destinatários que receberão o resultado da comparação. Para envio a mais de um e-mail use ponto e virgula (;) como separador.

Tag "**EspelhoPath**": Diretório onde os espelhos serão gerados. Recomendamos criar uma pasta exclusiva para os espelhos.

03: Configurações de envio de e-mail

Necessário que as configurações de "Envio de e-mail" estejam configuradas para que o e-mail seja enviado. Para maiores informações em como parametrizar seu envio de e-mail acesse: [Envio de email - LINHA RM](http://tdn.totvs.com.br/display/rm/Envio+de+email+-+LINHA+RM)

# Como Funciona:

---

false

**Detalhando a ferramenta**

O TOTVS Reports Compare, possui algumas opções que podem ser parametrizadas para sua execução. Listamos em vídeo logo abaixo, um explicativo do que é cada uma das opções disponíveis na ferramenta.

Vídeo: Detalhando o TOTVSReportsCompare600500false

**Geração de Espelhos**

Para iniciar o processo é necessário gerar os relatórios de "espelho". Estes servirão de referência (Gabaritos) para comparação. Cada espelho deve ser homologado pelo próprio usuário, validando se todas as informações foram geradas corretamente.

Como o espelho será utilizado como modelo, recomendamos que sempre seja regerado e revalidado quando houver alterações na estrutura, garantido assim a integridade e assertividade do processo.

Vídeo: Gerando Espelho(s)600500false

**Comparação de Relatórios**

Com os espelhos gerados, escolha os relatórios que serão comparados e clicando no botão comparar. Todos os relatórios serão comparados com seus respectivos espelhos. Ao final do processo, será exibido uma grade com o resultado da comparação.

Este resultado é passivo de ser enviado por e-mail, sendo necessário marcar o opção "enviar e-mail ao concluir" antes da comparação. No e-mail constará um arquivo com o resultado da comparação.

Vídeo: Comparando Relatório(s)

600500

Atenção

Somente relatórios genéricos (que **não** utilizam fonte de dados especificas) são gerados e consequentemente comparados.

---

Informamos que sistemas operacionais **Windows Server 2012 ou superiores** possuem em suas configurações regionais uma **diferença** na **formatação monetária** se comparado com os sistemas operacionais anteriores.

Sendo assim, relatórios “***espelhos***” que possuírem campos com formatação de moeda e que foram criados em sistemas operacionais inferiores a Windows Server 2012 darão divergência quando comparados com arquivos “***gerados***” em sistemas operacionais igual ou superior.

divs

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.15 ou Superiores

false

**Processo:** Totvs Reports Compare

falsefalse

**Status:** Finalizado

false

**Data:** 23/12//2016

false

**Autores:**
