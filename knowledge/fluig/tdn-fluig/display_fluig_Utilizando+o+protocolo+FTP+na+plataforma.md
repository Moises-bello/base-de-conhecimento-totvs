---
content_hash: 5f4976734c0b0c3501a8d3460828b64f7a01cec2695289d5718a68a4fb332caa
fetched_at: '2026-06-28T21:35:23.709129+00:00'
page_id: '258277580'
product: fluig
source: tdn-fluig
title: Utilizando o protocolo FTP na plataforma
type: documentation
url: https://tdn.totvs.com/display/fluig/Utilizando+o+protocolo+FTP+na+plataforma
version: 20
---

Atenção

Esta página é destinada para atualizações 1.6 e superiores do TOTVS Fluig Plataforma.

# Índice

true.\*ndicenone

# Objetivo

---

O objetivo deste guia é facilitar a compreensão quanto a utilização do protocolo FTP para publicação de documentos no TOTVS Fluig Plataforma.

# Procedimentos para utilização de protocolo FTP

---

Acompanhe o passo a passo a seguir:

false1true1Passo 1

* + Acessar a plataforma com o usuário wcmadmin → **Painel de Controle** → aba **WCM** → **Configurações do Sistema** → aba **Parâmetros da Plataforma**:
  + Clique em **OFF** para Habilitar servidor FTP:

[Clique aqui](http://tdn.totvs.com/pages/viewpage.action?pageId=257623022) e saiba mais sobre as configurações da plataforma

2Passo 2

* Altere o valor da **Porta do FTP** que será utilizado para o protocolo FTP. Por padrão a plataforma utiliza o valor 21. dois
* Também pode ser configurado uma faixa de portas conforme descrito abaixo:
  + **Faixa de Portas do FTP:** Faixa de portas utilizadas pelo FTP para publicação e publicação em pastas privadas.
  + **Faixa de portas FTP para pastas privadas:** Definir a faixa de portas usadas para a comunicação de FTP passivo.
  + **Porta FTP para pastas privadas:** Porta utilizada pelo FTP para publicação em pastas privadas.

* Clique em **Salvar**.
* Será necessário reiniciar os serviços do fluig.
3Passo 3

* Acesse o protocolo FTP a partir da ferramenta de sua preferência. Neste exemplo foi utilizado o software FileZilla.

1. 1. ***Host*:** informe o endereço do servidor, sem a porta de conexão HTTP. Exemplo: *localhost.*
   2. ***Username*:** informe o *login* do usuário do fluig.
   3. ***Password*:** informe a senha do usuário do fluig.
   4. ***Port*:** informe a porta configurada no item 2.

4Passo 4

* Utilizando o protocolo FTP, faça upload do arquivo desejado para o servidor.

 

5Passo 5

* Após realizar o *upload* para o servidor, o arquivo estará disponível no servidor no diretório de *upload* do usuário, aguardando ser publicado.

# Configurando portas passivas no FTP

---

Quando existir a necessidade de restringir as portas para a transferência dos arquivos, basta logar com o usuário **wcmadmin** e alterar o campo **Faixa de portas FTP para pastas privadas** em **Painel de Controle** → aba **WCM** → **Configurações do Sistema** → aba **Parâmetros da Plataforma:**

No valor, é possível passar uma porta, um grupo de portas ou um intervalo de portas.

**Exemplo:**

| Valor | Descrição |
| --- | --- |
| 0 | Qualquer porta disponível é utilizada como a porta passiva. |
| 123 | A porta 123 será usada como a porta passiva. |
| 123,133 | As portas 123 e 133 serão utilizadas como a porta passiva. |
| 123-125 | Qualquer porta de um intervalo de 123-125 será utilizada como a porta passiva. |
| 123-125, 127, 129-130 | Qualquer porta de um intervalo de 123-125, a porta 127 ou no intervalo de 129-130 será utilizada como a porta passiva. |
