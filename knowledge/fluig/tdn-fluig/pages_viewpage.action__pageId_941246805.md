---
content_hash: 85fca4589faf8b717c1285f01be87f3f82c4ab06c1600dec712613f60e343c89
fetched_at: '2026-06-28T21:35:31.532253+00:00'
page_id: '941246805'
product: fluig
source: tdn-fluig
title: ARQ - Como ajustar as configurações da plataforma da atualização 1.6.4 até
  1.8.2
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=941246805
version: 5
---

Fique atento!

Esta página é válida para as atualizações **1.6.4 até 1.8.2**do TOTVS Fluig.

Se você utiliza outra atualização, acesse:

* **Voyager (2.0) ou superior**: ;
* **1.6.0 até 1.6.3**: .

# Índice

trueÍndicenone

# Descrição

---

A plataforma possibilita a configuração de parâmetros do servidor de forma visual, na aba Parâmetros da Plataforma, ou através da API [System Configuration](https://api.fluig.com/old/resource_ConfigurationServiceRest.html).

# Arquivo de configuração

---

O arquivo de configuração é gerado durante o processo de instalação ou atualização. As configurações possíveis são as mesmas que eram disponibilizadas anteriormente (via *bindings* ou propriedades globais no arquivo **domain.xml**).

O arquivo de configuração está localizado em**[diretório\_instalação]/repository/wcmdir/config/configuration.properties** e utiliza o formato chave=valor.

Quando a plataforma é inicializada e o configuration.properties está presente na pasta config, será feita a persistência dos dados. Ao final deste processo ele é removido.

Atenção!

Caso desejar alterar um arquivo gerado automaticamente, é recomendado fazer *backup* do arquivo original.

# Recuperação das configurações

---

Alguma configuração feita foi perdida? Não se preocupe, a plataforma gera arquivos de backup das configurações!

Sempre que for realizada a configuração via tela ou API um arquivo de backup é gerado com as configurações suportadas.

Este arquivo é gerado em **[diretório\_instalação]/repository/wcmdir/config** e no nome do arquivo constará a data em que ele foi gerado, no formato **configuration.AAAAMMDD-HHmmss.properties**.

**Exemplo:** um arquivo de *backup* gerado no dia 01/12/2016 às 13:20:43, terá o nome configuration.20160201-132043.properties.

Se alguma alteração nos parâmetros impedir o acesso a plataforma, é possível recuperar a configuração anterior.

Para efetuar este procedimento:

* Faça uma cópia do arquivo de backup na data desejada para a mesma pasta;
* Nomeie o arquivo como **configuration.properties**;
* Reinicie a plataforma.

# Configurações do servidor disponíveis

---

As configurações de servidor passíveis de alteração estão relacionadas em [Parâmetros de configuração da plataforma](http://tdn.totvs.com/pages/viewpage.action?pageId=257623031).

Veja abaixo como é possível alterar propriedades pela *web* ou via API. 

# Configuração pela página Parâmetros da Plataforma

---

Para alterar algumas configurações chaves do servidor foi criado o recurso **Parâmetros da Plataforma** onde é possível visualizar as configurações atuais e alterar os parâmetros necessários.

Para visualizar a aba acesse a plataforma com o usuário **wcmadmin**, clique em **Painel de controle** → **WCM → Configurações do Sistema** → aba **Parâmetros da Plataforma**. 

Acesso via API

Também é possível realizar alterações nas configurações via API Pública, na documentação da API acesse a página **[System Configuration](https://api.fluig.com/old/resource_ConfigurationServiceRest.html)** para mais detalhes.

# Bloqueio de Clickjacking

---

A opção de Bloqueio de *Clickjacking* evita que ataques deste tipo sejam realizados na plataforma. Os ataques *Clickjacking* são executados inserindo uma página dentro de outra através de um elemento *iframe* em uma página *HTML* e interceptando eventos de mouse e teclado.

A configuração de **Bloqueio de *clickjacking*** está disponível no recurso de **Configurações do Sistema → Parâmetros da Plataforma** e vem habilitada por padrão.

Não é recomendado desativar esta opção, portanto altere esse parâmetro somente se tiver ciência dos riscos da vulnerabilidade.
