---
content_hash: d0123defbc15df7ab79ccb2dcbcd706eac2aafb7a860adb36219257cf5da96f5
fetched_at: '2026-06-29T00:09:12.708247+00:00'
page_id: '417700463'
product: rm
source: tdn-rm
title: Parametros
type: documentation
url: https://tdn.totvs.com/display/LRM/Parametros
version: 1
---

**Parametros**   
**Processo para gerar cadastro de cultura final ao finalizar a parcial**  
  Ao selecionar o parâmetro "Gerar o cadastro da cultura final ao finalizar a parcial" o sistema ira finalizar a cultura parcial automaticamente e será gerado um cadastro de cultura final.    
    
**Verificação de mensagem determinado por minutos**  
  Neste parâmetro ira configurar qual vai ser o tempo (Definidos em minutos) de verificação de mensagens novas, onde se surgira uma tela no canto direito inferior do aplicativo mostrando quantas mensagens não lidas o sistema tem.     
   
**Envio de Alerta para interrupção de antibiótico**   
  Quantidade de dias de defasagem para enviar o alerta de interrupção, podendo ser negativo, indicando que será enviado o alerta a quantidade definida de dias antes da interrupção do tratamento.  
   
**Parametrização da pressão atmosférica no APACHE II**  
"Pressão atmosférica para cálculo do APACHE II(GA-a O2)" nele o usuário vai informar qual é a pressão da sua região. Como padrão o sistema esta informando o valor de 760 que é a pressão atmosférica do nível do mar. Este parâmetro ira alterar a tela de APACHE II, mais precisamente o campo Gradiente A-a O2 que tem o seguinte calculo   
"gaao2 = (((fio2 \* (pressaoatmosferica - 47)) - (paco2 / 0.8)) - pao2);".  
Observação: O cálculo deste campo so vai se modificar após a alteração do parametro, porém os registros anteriores a modificação não irão se alterar.
