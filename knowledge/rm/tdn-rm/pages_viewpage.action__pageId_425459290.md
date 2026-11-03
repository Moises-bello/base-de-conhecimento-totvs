---
content_hash: 0e3f39194f5af8223c6e4d28cf3c763f8212ab8f1b3cdf9e9403307871106213
fetched_at: '2026-06-29T00:09:35.273660+00:00'
page_id: '425459290'
product: rm
source: tdn-rm
title: Linha RM x Microsoft Dynamics CRM - Configurações
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459290
version: 6
---

---

**Configurações**

Após o TOTVS Business Conector (TBC) ser instalado e configurado ele adiciona ao Menu principal do Microsoft CRM (MSCRM) um novo atalho "Integração", que contém toda área de configurações do TBC, Logs, entre outras informações.   
 Essa nova área é inserida após a importação de um arquivo sitemap.xml personalizado que adiciona esse novo item e todos os atalhos para as entidades base do TBC.  
 Ao se clicar no atalho Integração é possível visualizar várias novas entidades criadas para manter essas informações e configurações do TBC.

* **Usuários integração:** São armazenados quais usuários do MSCRM tem permissão para executar quais sincronizações. São vinculadas Funcionalidades a estes usuários e estas dão as permissões para quais sincronizações ele pode fazer. É necessário criar cada usuário e associando o *id* deste e atribuir as funções a ele.

* **Parâmetros:** Contém as principais configurações do TBC como: Nome de servidores, endereços de WebServices, dados de coligada para integração, proprietário padrão para registros incluídos no MSCRM, consultas para integração com RM, e-mail para avisos.

* **Logs:** Caso ocorra algum erro em alguma sincronização é criado um registro de Log contendo em qual sincronização ocorreu o erro, qual o horário e outras informações mais detalhadas sobre o erro.
* **Funcionalidades:** Contém os tipos de sincronização que podem ser realizadas. Estas Funcionalidades são associadas aos usuários para se determinar as permissões de sincronização de cada um. As funcionalidades são criadas pelo conector no momento da instalação.

* **Relacionamento Integração:** A entidade Relacionamento Integração armazena as informações sobre o mapeamento dos campos entre MSCRM e RM. Para um campo ser sincronizado entre os sistemas primeiro ele precisa ter esse mapeamento criado. Por padrão o Conector já vem com alguns mapeamentos básicos, mas outros campos de escolha do cliente podem sem facilmente mapeados.

      No momento da integração o conector consulta essa entidade para definir quais campos são mapeados, quais devem ser preenchidos, qual campo referencia qual e se esse campo será buscado no momento da criação e/ou atualização e se é permitido limpar o campo caso no outro sistema esteja em branco.  
  
 É definido o mapeamento entre os dois sistemas. É possível definir qual entidade do MSCRM sincroniza com qual entidade do RM, qual o campo, o tipo do campo e quando ocorrerá a integração (somente quando for incluir um novo registro, somente quando alterar, se o campo pode ser limpo).  
  
 Dentro desta entidade existe outra parte que é o Relacionamento DePara. Quando a *checkbox* estiver marcada no relacionamento integração (DePara Ativo) e a sincronização for realizada, o conector buscará os valores dentro de desses relacionamentos. Esse relacionamento é mapeado da seguinte forma: quando 1 no MSCRM então 001 no RM, por exemplo. Dessa forma quando o TBC encontrar um valor 1 no campo mapeado será feita a leitura do mapeamento e será passado para o RM o valor 001.  
  
 Atualmente o TBC está configurado para sincronizar os seguintes tipos de dados:

* Inteiro
* Texto
* Decimal
* Lookup (identicador Único)
* Data
* Lógico
* Moeda
* Picklist
* Float

* **Estados:** Armazena os estados cadastrados no RM. Pode ser utilizado para criar um relacionamento com outra entidade e evitar problemas com erros de digitação.

* **Municípios:** Armazena os municípios cadastrados no RM. Pode ser utilizado para criar um relacionamento com outra entidade.
