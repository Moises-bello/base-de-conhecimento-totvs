---
content_hash: 5d09595affe071b06b0782302ce2090377da183a2d6cd3e37294ab2a2b88b049
fetched_at: '2026-06-29T00:09:55.647644+00:00'
page_id: '448601553'
product: rm
source: tdn-rm
title: Código de Ajuste associado na Natureza de Operação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=448601553
version: 10
---

```
Ao incluir um Lançamento Fiscal ou Item do Lançamento, os defaults associados à natureza vão ser carregados automaticamente.
```

### Localização do Cadastro:

```
O cadastro do Código de Ajuste deve ser realizado no módulo do BackOffice → Gestão Fiscal em CADASTROS → MAIS → CÓDIGO DE AJUSTE
```

### **Associação Manual:**

```
Os Códigos de Ajuste podem ser vinculados à Natureza de Operação(CFOP) para que os mesmos sejam carregados automaticamente no Lançamento Fiscal. 
```

```

```

### **Associação Automática:**

```
Pode ser usado o processo  "Associação Códigos de Ajuste SPED Fiscal" para associar os ajustes na Natureza de Operação(CFOP):
```

Observação: Neste processo é possível *Desassociar* os Códigos de Ajuste, se necessário.

```
Deve ser criado um filtro para buscar os Códigos de Ajustes desejados, vão ser associados todos os códigos que foram localizados com o filtro informado.:
```

```
Processo executado:
```

```

```

```
Códigos associados:
```

**Preenchimento da Natureza:**

```
Neste exemplo foram carregados os Códigos de Ajuste cadastrados para o estado de São Paulo pois esse é o Estado parametrizado para o Cliente\Fornecedor. Os Ajustes que não são deste estado foram desconsiderados:
```

```
Lançamento:
```

### **Inclusão do item do lançamento fiscal:**

Os Ajustes serão carregados na inclusão do Item. De forma equivalente, os mesmos serão recuperados zerados e as fórmulas só serão executadas após salvar o lançamento fiscal.

##### 

**Atenção**: Caso o usuário edite algum valor, o sistema não executará as fórmulas para o Ajuste correspondente, sendo necessário zerar todos os valores do Ajuste a ser editado.

**Edição do lançamento/Item do lançamento**

```
Ao alterar um registro de Código de Ajuste de Lançamento/Item, os valores serão zerados. Os mesmos serão recalculados com as respectivas fórmulas, após salvar o Lançamento.  
O mesmo ocorre se os valores forem zerados manualmente. Assim, caso seja necessário executar novamente as fórmulas, basta zerar todos os valores.
```

**Escrituração Fiscal**

```
Ao Escriturar um Lançamento Fiscal, o sistema também carregará os Ajustes associados à natureza, já com os valores calculados pelas respectivas fórmulas.
```
