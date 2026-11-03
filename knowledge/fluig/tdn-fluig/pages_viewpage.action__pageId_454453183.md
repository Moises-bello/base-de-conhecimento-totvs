---
content_hash: 452c8c5e48c139169f38afcede5b6ab3a4aa70ca1280342ef36221ddd5cfd955
fetched_at: '2026-06-28T21:35:27.041241+00:00'
page_id: '454453183'
product: fluig
source: tdn-fluig
title: Configurar ambiente Linux para não utilizar o usuário root
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=454453183
version: 25
---

Índice

# Objetivo

---

Abaixo é apresentado um guia sobre como alterar as permissões e scripts para executar a plataforma e os serviços com um **usuário fluig**.

Nota:

Por conta da instalação dos serviços, o **processo de instalação** do TOTVS Fluig **deve ser** feito utilizando o **usuário root** e deve ser feito um **primeiro start** também utilizando o **usuário root**.

Nota:

Estas alterações serão desfeitas após o processo de atualização.

# Instalação/atualização da plataforma

---

Proceda a instalação ou atualização conforme o processo padrão que exige o usuário **root**. Para conferir os passos necessários, acesse .

## Usuário

---

Siga o procedimento abaixo para criar o usuário fluig. Utilize o comando abaixo:

Esse é um usuário de sistema, portanto não possuí senha ou interpretador de comando, logo não é possível realizar o login através dele. Porém se precisar realizar alguma atividade com o login fluig utilize o comando **sudo** no formato abaixo:

]]>

## Limites do usuário

---

Como o usuário criado não é mais o administrador, são definidos automaticamente alguns limites de recursos, que precisam ser expandidos, para tal edite o arquivo **/etc/security/limits.conf** e insira as linhas abaixo:

Lembrando que esse é um valor sugerido, em alguns casos o valor precisa ser aumentado, pois uma mensagem no *log* **"too many open files"** irá indicar que o valor limite de arquivos aberto não é suficiente.

## Scripts

---

Para a utilização do usuário adequado é necessário modificar os scripts de inicialização:

### Inicialização da plataforma

* Altere o arquivo **[diretório\_instalação]/appserver/bin/service/wildfly.conf**, substitua o valor da variável **JBOSS\_USER** por **fluig**, e.g:

Somente para a atualização Voyager (2.0) ou superiores:

* Se você utiliza a atualização **Voyager (2.0)** ou **superior** e o seu ambiente utiliza **systemd**, faça também o passo abaixo:
  + Altere o arquivo **/etc/systemd/system/fluig.service**  (ou dependendo **/etc/init.d/fluig**), substituindo o valor das variáveis **User** com valor **fluig**, e.g.:
  + Caso for instaldo o serviço fluig na porta abaixo de 1024 e sem proxy reverso, por exemplo na porta 80, precisa adicionar a variável **AmbientCapabilities** com o valor **CAP\_NET\_BIND\_SERVICE** abaixo da variável **User:**
  + Em seguida, execute este comando no terminal:

### Inicialização do serviço de indexação

* Altere o arquivo **/etc/init.d/fluig\_Indexer**, substitua o valor da variável RUNAS para **fluig**, e.g:

* No final do arquivo, substitua o bloco abaixo:

* pela linha a seguir:

* Altere o arquivo **[diretório\_instalação]/solr/bin/solr**, substituindo a linha abaixo:

* pela linha a seguir:

 /dev/null)
if [ "${running:-}" ]; then]]>

### Inicialização do serviço de Notificação em tempo Real

* Altere o arquivo **/etc/systemd/system/fluig\_RealTime.service** (ou dependendo **/etc/init.d/fluig\_RealTime**):

0.5falsesamples3fade1A partir da Voyager (2.0)

* Substitua o valor da variável **User** por **fluig**, e.g.:
* Caso for instalado o serviço fluig\_RealTime na porta abaixo de 1024 e sem proxy reverso, por exemplo na porta 77, precisa adicionar a variável **AmbientCapabilities** com o valor **CAP\_NET\_BIND\_SERVICE** abaixo da variável **User:**
* Em seguida, execute este comando no terminal:
2Versões anteriores

* Substitua a linha:

* pela linha abaixo:

* e substitua a linha:

> $LOG 2>&1 &]]>

* pela linha abaixo:

> $LOG 2>&1 &]]>

# Permissões

---

Para que os serviços consigam acessar os arquivos é necessário que o usuário fluig tenha acesso nos seguintes locais:

* Instalação da plataforma (ex: **/opt/fluig/\***)
  + Mude o dono de forma recursiva (-R) para o usuário **fluig**

* Volume de dados (ex: **/opt/volume/\***)
  + Mude o dono de forma recursiva (-R) para o usuário **fluig**

# Executando serviços em portas protegidas

---

Alguns sistemas operacionais Linux impedem que um usuário sem permissões administrativas utilize portas abaixo de 1024, isso impede por exemplo que o **fluig** aceite conexões na porta 80 e 443.

Isso pode ser mitigado de 2 formas:

* Usar uma ferramenta para realizar a tarefa de redirecionar as requisições para o fluig, como um  **(recomendado)**.
* Utilizar ferramentas de acordo com a distribuição, como por exemplo: **ufw** ou **firewall-cmd** ou **iptables**.
  + **Ubuntu Server 16.04 a 24.04**
    - Execute os comandos abaixo para liberar a porta 80 (fluig) e 7777 (fluig\_RealTime):
  + **Oracle Linux 7.x a 8.7 e 9.5 / CentOS 7.0 a 7.5 / Red Hat Enterprise Linux 9.5**
    - Execute os comandos abaixo para liberar a porta 80 (fluig) e 7777 (fluig\_RealTime):
  + **Oracle Linux 6.4 a 8.7 / CentOS 6.4 a 6.10 / Red Hat Enterprise Linux 6.4 a 8.7**  
    - Execute os comandos abaixo para liberar a porta 80 (fluig) e 7777 (fluig\_RealTime):
