---
content_hash: c73bb10c8be430c0054dd145385f8eff19051913ee0b6681bcc54593d48fd16f
fetched_at: '2026-06-29T00:09:37.209332+00:00'
page_id: '425459576'
product: rm
source: tdn-rm
title: TOTVS Obras e Projetos x BackOffice Protheus - Configuração e Parâmetros BackOffice
  Protheus
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459576
version: 2
---

**Configuração e Parâmetros BackOffice Protheus**

---

**Cadastro do Tipo de Entrada e Saída (TES) e Cadastro de Natureza**

Os cadastros de Tipo de Entrada e Saída (TES) e o cadastro de Natureza não são sincronizados para o RM, entretanto são obrigatórios para utilizar a integração.   
    
 Para realizar o cadastro de TES, acesse: Protheus | SigaFat (módulo padrão) | Atualizações | Cadastros | Tipos de Ent/Saida   
 Para realizar os cadastros de Natureza, acesse: Protheus | SigaFat (módulo padrão) | Atualizações | Cadastros | Natureza  
    
 ***Nota:*** *é necessário ter um cadastro de TES com código 501 para cima.*  
    
 **Parâmetros**

Na integração TOTVS Obras e Projetos x BackOffice Protheus existem parâmetros configuráveis necessários para o funcionamento correto da integração. Alguns parâmetros do BakcOffice Protheus referenciam as tabelas de cadastro, logo, o cadastro precisará ser feito antes de configurar o parâmetro.  
    
 Acesse: Módulo SigaCfg | Ambiente | Cadastros | Parâmetros  
 Localize cada parâmetro descrito abaixo e realize a configuração necessária.

* **MV\_INTPMS**

**Descrição:** Habilita integração de Gestão de Projetos para outros módulos do Protheus.   
 **Tipo:** Caracter.  
 **Possíveis Valores:**

* S (Sim)
* N (Não)  
   **Observação:** A configuração deste parâmetro é obrigatória.

* **MV\_RMCOLIG**

**Descrição:** Código da Coligada RM correspondente à Empresa Protheus corrente.  
 **Tipo:** Numérico.  
 **Observações:**

* A configuração deste parâmetro é obrigatória.
* Este parâmetro deve ser configurado para todas as Coligadas.

* **MV\_PMSRMLG**

**Descrição:** Habilita arquivo de log.  
 **Tipo:** Caracter.  
 **Possíveis Valores:**

* 0 (zero) - sem informação;
* 1 (um) - chamadas de Stored Procedure com erros;
* 2(dois) - todas as chamadas de Stored Procedure.  
   **Observações:**   
    - O arquivo de "log" não exibe chamadas feitas via Web Service.  
    - Este parâmetro é opcional e seu uso ocorre normalmente no inicio de implantação.  
    - Os logs das Stored Procedure podem ser visualizados na visão do Monitor da fila de Integração do TBC.

* **MV\_DIRLOG**

**Descrição:** Diretório onde serão armazenados os arquivos de Log.  
 **Tipo:** Caracter.  
 **Observação:** Este parâmetro é opcional e seu uso ocorre normalmente no inicio de implantação.

* **MV\_SLMNATR**

**Descrição:** Natureza padrão do Título a Receber.  
 **Tipo:** Caracter.  
 **Observações:**

* A configuração deste parâmetro é obrigatória;
* É necessário o cadastro prévio da natureza do título a receber.

* **MV\_SLMNATP**

**Descrição:** Natureza padrão do Título a Pagar.   
 **Tipo:** Caracter.   
 **Observações:**

* A configuração deste parâmetro é obrigatória;
* É necessário o cadastro prévio da natureza do título a pagar.

* **MV\_SLMNTPV**

**Descrição:** Natureza padrão do Pedido de venda.   
 **Tipo:** Caracter.   
 **Observações:**

* A configuração deste parâmetro é obrigatória.
* Neste parâmetro deve ser informado uma natureza do título a receber. Pode ser a mesma informada no parâmetro MV\_SLMNATR, ou pode ser criada uma nova.

* **MV\_SLMCOND**

**Descrição:** Condição de pagamento padrão.   
 **Tipo:** Caracter.   
 **Observações:**

* A configuração deste parâmetro é obrigatória;
* É necessário o cadastro prévio da condição de pagamento.
* Particularidades durante a medição de Contrato no TOTVS Obras e Projetos : Em um contrato que possui adiantamento, a condição de pagamento deve ter o parâmetro Adiantamento preenchido com valor igual a 'sim'. Nos contratos que não possuem adiantamento, é necessário que a condição de pagamento tenha o parâmetro Adiantamento preenchido com valor igual a 'não'.

* **MV\_SLMTS**

**Descrição:** Tipo de Saída (TES) padrão.   
 **Tipo:** Caracter   
 **Observações:**

* A configuração deste parâmetro é obrigatória;
* É necessário o cadastro prévio do tipo de saída (TES).
* Obrigatório existir cadastro do tipo saída com código 501.

* **MV\_SLMPROP**

**Descrição:** Produto padrão da despesa avulsa (título a pagar).   
 **Tipo:** Caracter.   
 **Observações:**

* A configuração deste parâmetro é obrigatória;
* É necessário o cadastro prévio do produto.

* **MV\_SLMCOMP**

**Descrição:** Define nome do usuário comprador default para alçada/WS.  
 **Tipo:** Caracter.  
 **Observação:** A configuração deste parâmetro é obrigatória quando a regra de alçada de compras estiver sendo utilizada no Protheus. Quando não estiver sendo utilizada o parâmetro não precisa ser configurado, mas pode ser utilizado.

* **MV\_SLMPRER**

**Descrição:** Define o prefixo dos títulos a receber.   
 **Tipo:** Caracter.   
 **Observações:**

* A configuração deste parâmetro é obrigatória.
* O prefixo deve ter até três letras.

* **MV\_SLMPREP**

**Descrição:** Define o prefixo dos títulos a pagar.  
 **Tipo:** Caracter.   
 **Observações:**

* A configuração deste parâmetro é obrigatória.
* O prefixo deve ter até três letras.
