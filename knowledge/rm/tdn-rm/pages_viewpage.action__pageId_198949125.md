---
content_hash: 17c92ee766b834a085042116cb770f1f96b02eab963941993d14799009148159
fetched_at: '2026-06-29T00:06:02.824235+00:00'
page_id: '198949125'
product: rm
source: tdn-rm
title: LinkedIn (Aplicativo)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=198949125
version: 14
---

# Índice:

---

.\*ndice:

# Pré-requisitos

---

2
complete
Linha RM atualizada até a versão 12.1.20

# Objetivos

---

Para que um sistema (RM) possa se integrar às redes sociais, é necessário a criação de um aplicativo nos provedores e gerar uma chave de acesso para a comunicação com a rede.

# Criando o App

---

1. Acessar <https://developer.linkedin.com/>
2. Selecione Meus aplicativos -> Criar Aplicativo
3. Preencher os dados necessários ao cadastro
4. Importante:  
   No grupo Autenticação -> Permissões padrão do aplicativo, marcar:

   * rw\_company\_admin
   * r\_emailaddress
   * r\_basicprofile
   * w\_share
5. Para verificar o App Key e Secret Key do LinkedIn, acesse <https://developer.linkedin.com/>
6. Selecione Meus Aplicativos -> <Nome do Aplicativo>
7. No grupo Autenticação -> Chaves de autenticação:

   * Código de cliente (APP Key)
   * Segredo de cliente (Secret Key)
8. Dentro do RM, Parâmetros Globais, aba Redes Sociais informar os dados dos respectivos aplicativos:
9. Ainda no Grupo Autenticação do aplicativo no LinkedIn, certifique-se de informar uma URL válida no campo:

OBS

A Url de Redirecionamento deverá ser a do google <https://www.google.com.br/>, porque ainda não foi exposto uma url de redirecionamento oficial.

Porém, caso o aplicativo seja para utilizar com o , nesta etapa, você deverá informar a as URI’s de redirecionamento do OAuth válidos.

Por exemplo:

* Para o portal do aluno de teste, nós poderíamos informar um endereço baseado em “localhost”, pois o Portal do Aluno de exemplo encontra-se na mesma máquina em que é feito a configuração (definimos o endereço: <http://localhost:8080/web/app/edu/PortalEducacional/>).
* Para o portal que está configurado com SSL informe o endereço correto de redirecionamento. (Neste exemplo usamos: <https://testeframe.com.br/RM12122/Login.aspx>)
Para maiores informações:

****[@FRAMEWORK](http://fluig.totvs.com/portal/p/10097/subject/rframework)****

**Canais de Atendimento**

**Chamado:** Através do Portal TOTVS - [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2-2-3-9-5 (Framework) ou 2-2-3-9-4 (BI)

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.20

false

**Processo:** Comunicação

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autores:**

.
