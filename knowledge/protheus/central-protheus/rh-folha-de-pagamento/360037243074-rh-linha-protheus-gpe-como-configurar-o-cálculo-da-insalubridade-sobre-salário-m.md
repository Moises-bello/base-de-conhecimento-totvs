---
article_id: 360037243074
category: RH - Folha de Pagamento
content_hash: 565ff127a4f5ffd0575a48eb1a8a4d80b199f7a8b32aef83b6c3d1af70cb41fa
fetched_at: '2026-06-28T22:44:13.293484+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como configurar o cálculo da insalubridade sobre
  salário minimo + verbas
type: support-article
updated_at: '2025-08-11T21:39:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037243074-RH-Linha-Protheus-GPE-Como-configurar-o-c%C3%A1lculo-da-insalubridade-sobre-sal%C3%A1rio-minimo-verbas
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26333926055831)** Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Como parametrizar o sistema para que o cálculo da insalubridade seja com base em salário minimo + verbas que devem compor a insalubridade?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Para que o cálculo da insalubridade seja com base em salário minimo + verbas, é necessário parametrizar no cadastro de sindicato conforme orientações abaixo:  
 **IMPORTANTE:** Esta alteração deve ser feita com a **Data Base do sistema** no **ultimo dia do mês anterior** ao mês do cálculo. Exemplo: **Cálculo** da folha de pagamento de **09/2024; Data base** do Sistema: **31/08/2024.  
  
1**. Entre na rotina Sindicato (caminho >Atualização >Cadastros >Sindicato) posicione no Sindicato em questão e clique em Alterar:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048773954)  
  
**2**. Entre na aba Peric./Insal. e deixe o campo selecionado abaixo conforme print:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048791334)  
  
**3**. Para as verbas que deverão fazer base para a Insalubridade, por exemplo a verba de falta, atraso, HE, entre outras, entrar no cadastro da verba e na aba Incidência, deixar o campo Insalubridade com SIM:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049691333)  
  
Lembrando que o valor do **salário****mínimo** deve ser informado em Manutenção de Tabelas > **S004**  
 **Saiba mais**

[Artigos Gestão de Pessoal](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867)

[RH - Linha Protheus - GPE - Como efetuar o cálculo de insalubridade utilizando o salário do cadastro + verbas com SIM para insalubridade como base de cálculo](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiLouPSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIB6mh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyMDQxOTIxMS1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1lZmV0dWFyLW8tYyVDMyVBMWxjdWxvLWRlLWluc2FsdWJyaWRhZGUtdXRpbGl6YW5kby1vLXNhbCVDMyVBMXJpby1kby1jYWRhc3Ryby12ZXJiYXMtY29tLVNJTS1wYXJhLWluc2FsdWJyaWRhZGUtY29tby1iYXNlLWRlLWMlQzMlQTFsY3VsbwY7CFQ6DnNlYXJjaF9pZEkiKTE0ODdhOWYxLTNmYzMtNDQ5Yi05YTU5LWQ5YzI5YTc3OGMyNwY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiAaBSSCAtIExpbmhhIFByb3RoZXVzIC0gR1BFIC0gQ29tbyBlZmV0dWFyIG8gY8OhbGN1bG8gZGUgaW5zYWx1YnJpZGFkZSB1dGlsaXphbmRvIG8gc2Fsw6FyaW8gZG8gY2FkYXN0cm8gKyB2ZXJiYXMgY29tIFNJTSBwYXJhIGluc2FsdWJyaWRhZGUgY29tbyBiYXNlIGRlIGPDoWxjdWxvBjsIVDoScmVzdWx0c19jb3VudGkC0Ac%3D--46662af06a15a38769b5cbba8d2125f0d2ab1934)

[RH - Linha Protheus - GPE - Cálculo de insalubridade sobre salário mínimo estadual](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXAzhqwxY6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBo2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzI1MDI4NTU2NDg5NDk1LVJILUxpbmhhLVByb3RoZXVzLUdQRS1DJUMzJUExbGN1bG8tZGUtaW5zYWx1YnJpZGFkZS1zb2JyZS1zYWwlQzMlQTFyaW8tbSVDMyVBRG5pbW8tZXN0YWR1YWwGOwhUOg5zZWFyY2hfaWRJIilkZTk5NWRhNS03Y2M5LTQzNGMtODgyYS1kZGJkYjg2YTcyYjkGOwhGOglyYW5raQo6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhJpbnNhbHVicmlkYWRlBjsIVDoScmVzdWx0c19jb3VudGkBnQ%3D%3D--076e98c55811415850b8ede747317158a229be86)

[RH - Linha Protheus - GPE - Quais as formas de parametrizar Periculosidade / Insalubridade](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiG28nUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBmGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MjI4NDI5NC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtUXVhaXMtYXMtZm9ybWFzLWRlLXBhcmFtZXRyaXphci1QZXJpY3Vsb3NpZGFkZS1JbnNhbHVicmlkYWRlBjsIVDoOc2VhcmNoX2lkSSIpZGU5OTVkYTUtN2NjOS00MzRjLTg4MmEtZGRiZGI4NmE3MmI5BjsIRjoJcmFua2kOOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSISaW5zYWx1YnJpZGFkZQY7CFQ6EnJlc3VsdHNfY291bnRpAZ0%3D--4668dbe12bd290cf08d798f5ece3bdaba498e7b2)

[RH - Linha Protheus - GPE - Insalubridade sobre salario mínimo + verbas - MV\_INSALVH = H com faltas](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwidOLnUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBomh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MTE5NDAxMy1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtSW5zYWx1YnJpZGFkZS1zb2JyZS1zYWxhcmlvLW0lQzMlQURuaW1vLXZlcmJhcy1NVi1JTlNBTFZILUgtY29tLWZhbHRhcwY7CFQ6DnNlYXJjaF9pZEkiKWI3Mzk3MjkyLWRlZGQtNGEzYi1hZmM4LWMyNTdmZWU2M2ZjNQY7CEY6CXJhbmtpDDoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiEmluc2FsdWJyaWRhZGUGOwhUOhJyZXN1bHRzX2NvdW50aQGd--a74900e78d97c1346341ce58f0547cbf26fba6c4)
