---
content_hash: 42f947c2283ecd7d06c3e5553c054e9711868b248817fa6d64157c8bbe03f744
fetched_at: '2026-06-29T00:05:54.261440+00:00'
page_id: '1077463753'
product: rm
source: tdn-rm
title: PI - Integração - RD Station - Campos Personalizados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1077463753
version: 3
---

### **Configuração de campos no RD Station integrados com o Portal de Imóveis:**

---

Nesta seção iremos visualizar como configurar os campos no RD Station que serão associados no Portal de Imóveis.

Para que este procedimento seja realizado é necessário acessar o RD Station, acessando o menu: Converter > Campos Personalizados

Neste momento selecione a opção: Criar campo personalizado

Utilizaremos como exemplo a inclusão do campo Estado Civil. Preenchendo os campos que serão relacionados. Ao final salve o registro incluído.

Acesse o portal de Imóveis, no menu: Integração > Campos personalizados

Clique em Sincronizar campos;

Os campos serão sincronizados e apresentados no Portal.   
Em nosso exemplo realize a edição do campo Estado Civil afim de que as chaves possam ser associadas as tabelas.

Associe os campos respectivos e em seguida clique em salvar.

**Configurando Campos Personalizados no RD Station CRM:**

Para facilitar a gestão de informações, clientes na versão 12.1.2606+ possuem uma tela exclusiva para a criação de campos personalizados diretamente no RD Station CRM, sem precisar sair do Portal.

**Como criar um novo campo pelo Portal:**

* Acesse o menu Integração > Campos personalizados.
* Clique no botão **Adicionar campo**.
* Preencha as informações:
  + **Entidade:** O sistema já preenche automaticamente como "Negociação".
  + **Campo:** Selecione a informação do Portal (ex: Empreendimento, Bloco, Unidade, Data da proposta) que alimentará o RD. Dica: Ao selecionar campos como "Empreendimento", o sistema carrega as opções ativas do seu banco de dados automaticamente.
  + **Label:** Digite o nome visual do campo para o corretor no RD.
  + **Tipo:** Defina se será Texto, Data, Seleção Única ou Múltipla.
  + Também poderá definir uma **ordem** para o campo personalizado e se depois de ser salvo, ao editar, se **p****ermitir adicionar nova opção**.
* Clique em **Criar**. O campo será gerado no RD Station CRM e no PI.

**Observação**: ao criar o campo personalizado diretamente pelo RD Station CRM ele será automaticamente integrado ao Portal de imóveis.
