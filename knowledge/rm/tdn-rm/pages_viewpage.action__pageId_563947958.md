---
content_hash: 58672e27fd3c20d619553270ae185931b3989c088b5985e425ca842463829c39
fetched_at: '2026-06-29T00:10:51.232368+00:00'
page_id: '563947958'
product: rm
source: tdn-rm
title: Portal de Imóveis - Backend - Sincronizar
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=563947958
version: 15
---

**Definição:**

---

A sincronização desempenha um papel crucial no processo de unificação dos dados entre o sistema RM e o Portal de Imóveis. Sua importância primordial reside na habilidade de buscar e manter informações diretamente no sistema RM, assegurando a consistência desses registros nos cadastros do Portal de Imóveis.

Este procedimento garante que as informações permaneçam continuamente atualizadas e coerentes entre os dois sistemas, tornando possível uma integração eficaz e absolutamente necessária. O objetivo deste material é orientá-lo através desse processo de sincronização, proporcionando uma compreensão completa e um uso eficiente dessa funcionalidade essencial para a operação integrada de ambos os sistemas.  
  
É possível sincronizar os seguintes dados do RM, seja de forma completa ou individual:  
01. Empreendimentos  
02. Blocos  
03. Unidades  
04. Vagas  
05. Tabela de Preço  
06. Tabela de Preço (Preço unidades)  
07. Modalidade Venda  
08. Componente x Modalidade  
09. Modalidade x Tabela de Preço  
10. Região  
11. Mídia  
12. Profissão  
13. Comunhão de Bens  
14. Vendas Distratadas  
15. Cidades  
16. Parâmentros  
17. Aditivo de Troca de Unidade

**Totvs Sign:** Consulta o serviço disponibilizado do TOTVS Assinatura Eletrônica *GlbTotvsSignParametrosData* e verifica se esta integração está ativa. Se sim, passa a disponibilizar a integração com o TOTVS Sign na assinatura de documentos digitais.

---

**Execução da sincronização:**1. Acesse Backend > Sincronizar

2. Ao visualizar a tela de sincronização, o usuário terá a opção de sincronizar cada tarefa separadamente. No entanto, se preferir, também poderá executar todas as tarefas de uma só vez, o que estará disponível ao final da página.

3. Após concluir a sincronização, o portal irá exibir o Log de sincronização em uma página caso o usuário queira consistir alguma informação.

Observações:

* **A partir da Versão 12.1.2302**, as tabelas do Portal serão convertidas internamente na base RM sob o nome "XPI". Exemplos:  
  - XPIUSUARIO  
  - XPIPARAMETRO  
  - XPIMENU  
  - XPIEMPREENDIMENTO ...
* **A partir da Versão 12.1.2402**, a sincronização será efetuada através do menu "Utilitários" *(opção "Sincronização Portal Imóveis")* diretamente no sistema RM. Para obter mais informações, consulte a página: **[TOTVS Construção Gestão de Imóveis - Utilitários - Sincronismo portal de Imóveis 12.1.2402](https://tdn.totvs.com/pages/viewpage.action?pageId=794362068)**
* Ressaltamos também que a partir da versão 12.1.2402, a exibição da sincronização no portal de imóveis passa a ser apenas informativa, mostrando os status da última sincronização das tabelas.
