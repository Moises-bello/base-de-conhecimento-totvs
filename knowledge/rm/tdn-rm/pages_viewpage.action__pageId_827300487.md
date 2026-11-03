---
content_hash: b2fde3583c8faf993c413d8aeb25826dacf9164db4bad7714d24c8fcc87da394
fetched_at: '2026-06-29T00:11:48.715983+00:00'
page_id: '827300487'
product: rm
source: tdn-rm
title: Medidor - Importar medições
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=827300487
version: 9
---

---

### **Objetivo**

O processo de "Importar Medições" possibilita adicionar dados de medições no sistema a partir de um arquivo Excel. Ao usar esse processo, os usuários podem configurar e importar medições diretamente do arquivo Excel sem precisar digitar manualmente.  ***Processo disponível a partir da versão 12.1.2406 (e superiores)***

### **Configurando o processo de importação**

---

No menu condomínio, clique em Medidor e em seguida no menu processos selecione: **Importar Medições.**  
Ao acessar esta tela serão apresentada as opções:

* **Arquivo da Planilha:** informe o diretório onde a planilha excel encontra-se salva com os dados das Medições;
* **Importar por:**
  + ***Identificador:*** Será utilziado o Identificador da medição para importação;
  + ***Número do Equipamento:*** Será utilizado o número do equipamento para realizar a importação.   
    *Observação: Caso o número do equipamento no arquivo a ser importado não existir no sistema, uma mensagem de log será apresentada ao usuário após a importação, informando que o medidor não foi identificado.*
* **Células dos campos:** Refere-se as configurações que serão lidas na planilha para que a sua importação seja realizada.
  + ***Nome da Planilha:*** informe o nome da planilha que é informada no excel (veja exemplo na imagem abaixo);
  + **Preencha nos campos os valores respectivos a cada célula de sua planilha:** *N° Identificação, N° equipamento, Competência, Data Medição, Medição.*
  + ***Substituir medições existentes:*** Quando marcada esta opção possibilita substituir os dados e valores em uma medição já existente.
  + ***Visualizar:*** Esta opção deverá ser selecionada para que os dados do arquivo Excel possam ser carregados na visão para validação e importação;
* ***Pré-Visualização dos dados:*** Possibilitará o usuário visualizar os dados que serão importados no sistema.
* ***Executar:*** Ao selecionar esta opção o sistema irá realizar o processo de importação e ao final será apresentado o Log de importação para o usuário.

*Se o usuário não possuir permissão para executar a importação de medições, será necessário conceder acesso no perfil do usuário. Isso pode ser feito através do seguinte caminho: Gestão de Imóveis > Condomínio > Fechamento do Condomínio > Medidor > Inserir.*
