---
article_id: 360022631391
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: fdf71d1612ec2c92e3dcb1bb8705a14f36c478de0d7d486a68628d60541dddac
fetched_at: '2026-06-28T22:38:32.659628+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: MP-FAT-Término do horário de Verão
type: support-article
updated_at: '2021-04-28T15:55:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022631391-MP-FAT-T%C3%A9rmino-do-hor%C3%A1rio-de-Ver%C3%A3o
---

**Dúvida**

Como ajustar o ambiente para o término do horário de verão?  
  
**Ambiente**

Microsiga Protheus -  a partir da  versão 11.80.  
  
**Solução**

Conforme medida sancionada por nosso atual presidente da Republica, desde o ano de 2019 não haverá mais a adoção do horário de Verão.

Desta forma, se houver alguma alteração de horário do Servidor de forma automática, proceda da seguinte forma:

**1 -** Verifique o conteúdo do parâmetro **MV\_HORARMT:**

**1.1 -** Estando o conteúdo do parâmetro como **1** (Gravar na Nota o horário registrado na máquina em que está acessando o Smartclient), ajuste o horário diretamente na máquina  e desmarque a opção da configurações de fuso horário "Ajustar automaticamente o relógio para Horário de Verão".

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049607933/mceclip0.png)

**1.2 -** Estando o conteúdo do parâmetro como **2** (Gravar na nota a hora que está registrado no servidor onde está instalado o Protheus), efetuar as alterações do horário atual no Servidor, conforme as indicações anteriores. Caso o Servidor esteja em Cloud Totvs, solicite ao atendimento Cloud efetuar o ajuste do horário do Servidor Protheus.

**1.3 -** Estando o conteúdo do parâmetro como **3** (Gravar na Nota o horário do servidor, mas adaptar ao fuso horário de cada Filial -> Esta opção é utilizada APENAS para empresas que emitem em uma mesma máquina NFs para diversas Filiais, em que, uma possui fuso horário diferente da outra)

Mantenha a data do horário de verão relacionado ao ano passado , onde o parâmetro **MV\_HVERAOI** , que indica o Inicio do horário de verão, receberá  **20181104** e o parâmetro **MV\_HVERAOF**, este indica quando o horário de verão deverá Terminar, receberá **20190216**, em formato de data americana**.**

**2.** Demais ajustes deverão ser efetuados na rotina de transmissão de nota:

**2.1 - Transmissão NFe-Sefaz (SPEDNFE):**

**2.1a -** Ações relacionadas-> parâmetros-> NFe;

**2.1b -** Altere o parâmetro de horário de verão para NÃO e certifique- se que o fuso horário esta correto;

**2.1c -** Salve as configurações.

**2.2 - Parâmetro** **MV\_HVERAO:**deixar como **.F.**

**2.3 - TSS:**

**2.3a -** No Appserver.ini do seu TSS, tag **SPED\_HVERAO,** deixar como 2;  
**2.3b -** Após a alteração, reinicie o serviço do seu TSS.

**Se o ERP Microsiga Protheus estiver com o horário incorreto, será necessário ajustar o horário do servidor e máquina local com horário correto. em caso de servidores Slaves, é preciso garantir que todos os Slaves estejam com os horários ajustados conforme o servidor Master.**

**OBS: Verifique se o MATA461 está atualizado, pois, a falta de atualização pode implicar na gravação incorreta do campo F2\_HORA, abaixo segue o link  da página de pacote de acumulados do módulo faturamento:**

<https://tdn.totvs.com/pages/releaseview.action?pageId=521997859>

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099955013/mceclip0.png)

Em caso de dúvidas, consulte a FAQ no TDN:  [**MP-FAT-Como corrigir rejeição 578 e 703**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115001380867--MP-FAT-Como-corrigir-rejei%C3%A7%C3%A3o-578-e-703-?source=search)
