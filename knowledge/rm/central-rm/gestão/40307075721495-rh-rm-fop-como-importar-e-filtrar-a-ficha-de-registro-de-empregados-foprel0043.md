---
article_id: 40307075721495
category: Gestão
content_hash: 1881004bb933ffa4733c424597913085f243e4dc0b1853db0f168637cf0db889
fetched_at: '2026-06-28T22:46:48.197396+00:00'
product: rm
section_id: 1500000861162
source: central-rm
title: 'RH - RM - FOP: Como importar e filtrar a Ficha de Registro de Empregados (FOPREL0043)'
type: support-article
updated_at: '2026-05-27T18:39:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40307075721495-RH-RM-FOP-Como-importar-e-filtrar-a-Ficha-de-Registro-de-Empregados-FOPREL0043
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40307075700119) Tempo aproximado para leitura: 00:03:00 min  
  
**Dúvida**  
Como realizar a importação do relatório padrão de Ficha de Registro via TOTVS Compartilhamento e aplicar filtros por Chapa ou Tipo de Demissão?  
  
**Ambiente**  
TOTVS RH (Linha RM) - TOTVS Folha de Pagamento (Labore) - RM Reports - Todas as versões.  
  
**Solução**  
Para disponibilizar e gerar o relatório em sua base, siga os passos abaixo:  
**1. Importação via TOTVS Compartilhamento:**

* No campo **Buscar**, digite o código do relatório: `FOPREL0043`.
* Clique em **Pesquisar**.
* Selecione o registro encontrado (*FOPREL0043 - Ficha de Registros de Empregados.TotvsReport*) e clique no botão **Download**.
* Na janela seguinte, selecione **Importar** para que o relatório seja enviado diretamente para o seu **RM Reports**.  
    
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40312867017239)  
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40312867020951)  
    
  Selecione um por um para importar sentença e substituir se existir arquivo:  
    
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40312912064791)  
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40312867024023)  
    
  **2. Localização e Geração no RM Reports:**  
  Após importar, o relatório estará disponível na sua lista de objetos gerenciais.

  + **O que fazer:** Vá em **Gestão > RM Reports**. Use o filtro para achar o `FOPREL0043`, marque o "check" ao lado dele e clique em gerar.  
      
    ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40312867025047)  
    ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40312912067351)

    **3. Configurando o Filtro (Chapa ou Demissão):**  
    Para não emitir a ficha de todos os funcionários de uma vez, você precisa restringir a busca.
* **O que fazer:** Na tela de geração, clique nos **três pontinhos (...)** ao lado de "Chapa do Funcionário".  
    
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40312912069783)  
    
  **4. Editando a Expressão do Filtro:**  
  Aqui é onde você define quem será impresso.
* **O que fazer:** Clique em **Modificar**. Na tela de expressão, você pode trocar o campo para `Chapa do Funcionário` ou `Tipo de Demissão` e escolher o valor desejado.  
    
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40312867027735)  
    
  **Filtro por Chapa:** Mude a expressão de `IS NOT NULL` (que traz todo mundo) para `IGUAL A` (e digite o número da chapa).  
    
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40312867030551)  
    
  **Filtro por Transferência:** Se for para demissões por transferência, use o campo `Tipo de Demissão` e filtre pelo código de transferência da sua empresa.  
    
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40312867031191)  
    
  **Saiba mais:**  
  [RH - RM - FOP- Importação de relatórios e layouts através do Totvs Compartilhamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7781155867543-RH-RM-FOP-Importa%C3%A7%C3%A3o-de-relat%C3%B3rios-e-layouts-atrav%C3%A9s-do-Totvs-Compartilhamento)
