---
article_id: 360029018071
category: Comércio Exterior - Easy Export Control - Embarque
content_hash: 189d64500b31e2b07f82993f55c7d13b6849d2882163ccbb230d05dd360a3b27
fetched_at: '2026-06-28T22:36:39.193271+00:00'
product: protheus
section_id: 1500001549322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Inicializador
  padrão do campo EYY_VM_DES
type: support-article
updated_at: '2022-06-09T20:47:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029018071-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Inicializador-padr%C3%A3o-do-campo-EYY-VM-DES
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Ocorrência**No embarque de Exportação apresenta a mensagem:  
*Help: INITLINE*  
Problema: Erro no inicializador padrão do campo (**EYY\_VM\_DES**).   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Export Control* – A partir da versão 12.1.17  
  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse o SIGACFG selecione em Base de Dados / Dicionário / Base de Dados:  
![](https://totvssuporte.zendesk.com/attachments/token/K3wGglADfASowa7xpmS0HOmLR/?name=inline-1172971682.png)​  
  
2. Selecione em Dicionário de Dados e clique na Lupa para buscar a tabela EYY:  
![](https://totvssuporte.zendesk.com/attachments/token/SbuO5GBtkXxqwhtGiVh4iOYNN/?name=inline-1303487861.png)​  
  
![](https://totvssuporte.zendesk.com/attachments/token/9IvrTzCupBpYH5Q89wA0VtabD/?name=inline-895632558.png)​  
  
3. Ao posicionar na tabela selecione o Editar  
![](https://totvssuporte.zendesk.com/attachments/token/hfatlzvL543tPhUzDonhlp0ZQ/?name=inline920133802.png)​  
  
4. Clique no + e selecione a opção Campos:  
![](https://totvssuporte.zendesk.com/attachments/token/U3QekCoBIyb2zEVTc6pydIIPV/?name=inline-1160462317.png)​  
![](https://totvssuporte.zendesk.com/attachments/token/JmlEwA2t7j2E4HfO4J9oUA9LF/?name=inline1311118379.png)​  
  
5. Selecione novamente a Lupa e busque o campo EYY\_VM\_DES   
![](https://totvssuporte.zendesk.com/attachments/token/BDw5jiEVV9IC6WxbLtSGiUhLo/?name=inline685534694.png)​  
  
6. Selecione a opção editar para alterar o campo  
![](https://totvssuporte.zendesk.com/attachments/token/Y7jmqkQ8x8wAkMRzaX5xRiiP2/?name=inline-421124751.png)​  
  
7. Na aba opções , retire o conteúdo do campo Inic.Padrão e clique em Salvar.  
![](https://totvssuporte.zendesk.com/attachments/token/e9g3QSfZ1Ah7ZCqihv9b6MPQq/?name=inline-792084779.png)  
  
8. Após selecione o símbolo verde:  
![](https://totvssuporte.zendesk.com/attachments/token/kgNzC68kvDs75dL4FcSXSCdUB/?name=inline897446885.png)​  
  
9. E na próxima tela selecione o símbolo do disquete para salvar alteração:   
![](https://totvssuporte.zendesk.com/attachments/token/OyhwFHp97NSCm6vbNyjrf4Hxh/?name=inline1585759511.png)  
  
Após efetue o procedimento novamente.
